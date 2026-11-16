
from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation


class ExpenseService:

    def __init__(self, excel_manager):

        self.excel = excel_manager

        self.ws_fifo = self.excel.get_sheet("Партії Fifo")
        self.ws_expense = self.excel.get_sheet("Видаток")

        # Індекси колонок FIFO
        self.fifo_columns = {
            "date": 1,
            "code": 2,
            "lot": 3,
            "initial_quantity": 4,
            "remaining_quantity": 5,
            "price": 6,
            "remaining_value": 7
        }

        # Індекси колонок видатку
        self.expense_columns = {
            "date": 1,
            "code": 2,
            "name": 3,
            "unit": 4,
            "quantity": 5,
            "price": 6,
            "value": 7,
            "lot": 8
        }

    # -------------------------------------------------
    # ФІНАНСОВІ РОЗРАХУНКИ
    # -------------------------------------------------

    @staticmethod
    def money(value):

        return Decimal(str(value)).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

    @staticmethod
    def to_decimal(value, field_name):

        try:
            result = Decimal(str(value))

        except (InvalidOperation, ValueError, TypeError):
            raise ValueError(
                f"Некоректне числове значення: {field_name}"
            )

        if not result.is_finite():
            raise ValueError(
                f"Поле {field_name} повинно бути скінченним числом"
            )

        return result

    # -------------------------------------------------
    # РОБОТА З ДАТОЮ ТА ЧАСОМ
    # -------------------------------------------------

    @staticmethod
    def get_date(value):

        if isinstance(value, datetime):
            return value

        if isinstance(value, date):
            return datetime.combine(
                value,
                datetime.min.time()
            )

        if isinstance(value, str):

            try:
                return datetime.fromisoformat(
                    value.strip()
                )

            except ValueError:
                pass

            # Підтримка формату YYYY-MM-DD-HH-MM
            try:
                return datetime.strptime(
                    value.strip(),
                    "%Y-%m-%d-%H-%M"
                )

            except ValueError:
                pass

            # Підтримка дати без часу
            try:
                return datetime.combine(
                    date.fromisoformat(value.strip()),
                    datetime.min.time()
                )

            except ValueError:
                pass

        raise ValueError(
            f"Некоректна дата та час: {value}"
        )

    # -------------------------------------------------
    # ЗБІР FIFO-ПАРТІЙ
    # -------------------------------------------------

    def get_fifo_lots(self, code, expense_date):

        fifo = self.fifo_columns

        lots = []

        for row in range(2, self.ws_fifo.max_row + 1):

            lot_code = self.ws_fifo.cell(
                row,
                fifo["code"]
            ).value

            if lot_code is None:
                continue

            if str(lot_code).strip() != code:
                continue

            # Залишок партії
            remaining = self.to_decimal(
                self.ws_fifo.cell(
                    row,
                    fifo["remaining_quantity"]
                ).value or 0,
                "Залишок партії"
            )

            if remaining < 0:
                raise ValueError(
                    f"Від'ємний залишок у FIFO, рядок {row}"
                )

            if remaining == 0:
                continue

            # Дата та час надходження
            lot_date = self.get_date(
                self.ws_fifo.cell(
                    row,
                    fifo["date"]
                ).value
            )

            # Не використовуємо майбутні партії
            if lot_date > expense_date:
                continue

            # Ціна партії
            price = self.to_decimal(
                self.ws_fifo.cell(
                    row,
                    fifo["price"]
                ).value,
                "Ціна партії"
            )

            if price < 0:
                raise ValueError(
                    f"Від'ємна ціна у FIFO, рядок {row}"
                )

            lots.append({

                "row": row,

                "date": lot_date,

                "lot": self.ws_fifo.cell(
                    row,
                    fifo["lot"]
                ).value,

                "remaining": remaining,

                "price": price

            })

        # FIFO: дата, час та початковий порядок рядків
        lots.sort(
            key=lambda item: (
                item["date"],
                item["row"]
            )
        )

        return lots

    # -------------------------------------------------
    # ФОРМУВАННЯ ПЛАНУ СПИСАННЯ
    # -------------------------------------------------

    def prepare_allocations(self, lots, quantity):

        available = sum(
            (lot["remaining"] for lot in lots),
            Decimal("0")
        )

        if available < quantity:

            raise ValueError(
                f"Недостатньо товару!\n"
                f"Потрібно: {quantity}\n"
                f"Доступно: {available}"
            )

        remaining_to_write_off = quantity

        allocations = []

        for lot in lots:

            if remaining_to_write_off <= 0:
                break

            write_quantity = min(
                lot["remaining"],
                remaining_to_write_off
            )

            price = lot["price"]

            value = self.money(
                write_quantity * price
            )

            new_remaining = (
                lot["remaining"] - write_quantity
            )

            allocations.append({

                "row": lot["row"],

                "lot": lot["lot"],

                "quantity": write_quantity,

                "price": price,

                "value": value,

                "new_remaining": new_remaining

            })

            remaining_to_write_off -= write_quantity

        if remaining_to_write_off != 0:
            raise ValueError(
                "Не вдалося повністю розподілити списання"
            )

        return allocations

    # -------------------------------------------------
    # ЗАПИС СПИСАННЯ В EXCEL
    # -------------------------------------------------

    def save_allocations(
        self,
        allocations,
        product,
        expense_date
    ):

        fifo = self.fifo_columns

        original_expense_max_row = self.ws_expense.max_row

        original_values = {}

        try:

            for item in allocations:

                fifo_row = item["row"]

                # Запам'ятовуємо попередні значення
                original_values[fifo_row] = {

                    fifo["remaining_quantity"]:
                        self.ws_fifo.cell(
                            fifo_row,
                            fifo["remaining_quantity"]
                        ).value,

                    fifo["remaining_value"]:
                        self.ws_fifo.cell(
                            fifo_row,
                            fifo["remaining_value"]
                        ).value

                }

                new_quantity = item["new_remaining"]

                new_value = self.money(
                    new_quantity * item["price"]
                )

                # Оновлюємо кількість
                self.ws_fifo.cell(
                    fifo_row,
                    fifo["remaining_quantity"]
                ).value = float(new_quantity)

                # Оновлюємо вартість
                self.ws_fifo.cell(
                    fifo_row,
                    fifo["remaining_value"]
                ).value = float(new_value)

                # Запис видатку
                expense_row = [

                    expense_date,

                    product["code"],

                    product["name"],

                    product["unit"],

                    float(item["quantity"]),

                    float(item["price"]),

                    float(item["value"]),

                    item["lot"]

                ]

                self.ws_expense.append(expense_row)

                # Формат дати та часу
                self.ws_expense.cell(
                    self.ws_expense.max_row,
                    1
                ).number_format = "dd.mm.yyyy hh:mm"

            # Збереження Excel
            self.excel.save()

        except Exception:

            # Відновлення FIFO
            for row, values in original_values.items():

                for column, value in values.items():

                    self.ws_fifo.cell(
                        row,
                        column
                    ).value = value

            # Видалення доданих записів видатку
            current_max_row = self.ws_expense.max_row

            if current_max_row > original_expense_max_row:

                self.ws_expense.delete_rows(
                    original_expense_max_row + 1,
                    current_max_row - original_expense_max_row
                )

            raise

    # -------------------------------------------------
    # ОСНОВНИЙ МЕТОД СПИСАННЯ FIFO
    # -------------------------------------------------

    def write_off(
        self,
        code,
        quantity,
        expense_date=None
    ):

        code = str(code).strip()

        if not code:
            raise ValueError(
                "Не вказано код товару"
            )

        # Перевірка кількості
        quantity = self.to_decimal(
            quantity,
            "Кількість списання"
        )

        if quantity <= 0:
            raise ValueError(
                "Кількість списання повинна бути більшою за 0"
            )

        # Дата та час списання
        if expense_date is None:

            expense_date = datetime.now()

        else:

            expense_date = self.get_date(
                expense_date
            )

        # Перевіряємо товар
        product = self.excel.get_product(code)

        if product is None:
            raise ValueError(
                f"Товар {code} не знайдено"
            )

        # Перевірка реквізитів товару
        for field in ("code", "name", "unit"):

            if product.get(field) is None:
                raise ValueError(
                    f"У довіднику товару відсутнє поле: {field}"
                )

        # Отримуємо FIFO-партії
        lots = self.get_fifo_lots(
            code,
            expense_date
        )

        if not lots:
            raise ValueError(
                f"Немає доступних FIFO-партій товару {code}"
            )

        # Формуємо план списання
        allocations = self.prepare_allocations(
            lots,
            quantity
        )

        # Записуємо списання
        self.save_allocations(
            allocations,
            product,
            expense_date
        )

        # Загальна вартість
        total_value = sum(
            (item["value"] for item in allocations),
            Decimal("0")
        )

        return {

            "code": product["code"],

            "name": product["name"],

            "quantity": quantity,

            "total_value": total_value,

            "allocations": allocations

        }
