
from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP


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

    @staticmethod
    def money(value):

        return Decimal(str(value)).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

    @staticmethod
    def get_date(value):

        if isinstance(value, datetime):
            return value.date()

        if isinstance(value, date):
            return value

        if isinstance(value, str):
            return date.fromisoformat(value)

        raise ValueError("Некоректна дата партії")

    def write_off(self, code, quantity, expense_date=None):

        code = str(code).strip()
        quantity = Decimal(str(quantity))

        if quantity <= 0:
            raise ValueError("Кількість списання повинна бути більшою за 0")

        if expense_date is None:
            expense_date = date.today()

        if isinstance(expense_date, str):
            expense_date = date.fromisoformat(expense_date)

        if not isinstance(expense_date, date):
            raise ValueError("Некоректна дата видатку")

        # Перевіряємо наявність товару в довіднику
        product = self.excel.get_product(code)

        if product is None:
            raise ValueError(f"Товар {code} не знайдено")

        # Отримуємо FIFO-партії потрібного товару
        fifo = self.fifo_columns

        lots = []

        for row in range(2, self.ws_fifo.max_row + 1):

            lot_code = self.ws_fifo.cell(
                row, fifo["code"]
            ).value

            if str(lot_code).strip() != code:
                continue

            remaining = Decimal(str(
                self.ws_fifo.cell(
                    row, fifo["remaining_quantity"]
                ).value or 0
            ))

            if remaining <= 0:
                continue

            lot_date = self.get_date(
                self.ws_fifo.cell(
                    row, fifo["date"]
                ).value
            )

            if lot_date > expense_date:
                continue    

            lots.append({
                "row": row,
                "date": lot_date,
                "lot": self.ws_fifo.cell(
                    row, fifo["lot"]
                ).value,
                "remaining": remaining,
                "price": Decimal(str(
                    self.ws_fifo.cell(
                        row, fifo["price"]
                    ).value
                ))
            })

        # Сортування за датою та початковим порядком рядків
        lots.sort(key=lambda item: (item["date"], item["row"]))

        # Перевіряємо загальну доступну кількість
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

        # Формуємо план списання, не змінюючи Excel
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

            value = self.money(write_quantity * price)

            allocations.append({
                "row": lot["row"],
                "lot": lot["lot"],
                "quantity": write_quantity,
                "price": price,
                "value": value,
                "new_remaining": lot["remaining"] - write_quantity
            })

            remaining_to_write_off -= write_quantity

        # Оновлюємо партії та записуємо видаток
        for item in allocations:

            fifo_row = item["row"]

            new_quantity = item["new_remaining"]

            new_value = self.money(
                new_quantity * item["price"]
            )

            self.ws_fifo.cell(
                fifo_row,
                fifo["remaining_quantity"]
            ).value = float(new_quantity)

            self.ws_fifo.cell(
                fifo_row,
                fifo["remaining_value"]
            ).value = float(new_value)

            # Окремий запис для кожної партії
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

        # Загальна вартість списання
        total_value = sum(
            (item["value"] for item in allocations),
            Decimal("0")
        )

        # Зберігаємо Excel
        self.excel.save()

        return {
            "code": product["code"],
            "name": product["name"],
            "quantity": quantity,
            "total_value": total_value,
            "allocations": allocations
        }
