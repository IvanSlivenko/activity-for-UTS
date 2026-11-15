
from pathlib import Path
from openpyxl import load_workbook
from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation


class ExcelManager:

    def __init__(self, file_path="db.xlsx"):

        self.file_path = Path(file_path)

        if not self.file_path.exists():
            raise FileNotFoundError(
                f"Excel-файл не знайдено: {self.file_path}"
            )

        self.wb = load_workbook(self.file_path)

        # Назви аркушів та їхні обов'язкові колонки
        self.required_sheets = {

            "Товари": [
                "Код",
                "Назва",
                "Одиниця виміру"
            ],

            "Надходження": [
                "Дата",
                "Код",
                "Назва",
                "Одиниця виміру",
                "Кількість",
                "Ціна",
                "Вартість"
            ],

            "Видаток": [
                "Дата",
                "Код",
                "Назва",
                "Одиниця виміру",
                "Кількість",
                "Ціна",
                "Вартість",
                "НомерПартії"
            ],

            "Залишки": [
                "Дата",
                "Код",
                "Назва",
                "Одиниця виміру",
                "Кількість",
                "Вартість"
            ],

            "Партії Fifo": [
                "ДатаНадходження",
                "Код товару",
                "НомерПартії",
                "ПочатковаКількість",
                "Кількість залишку",
                "Ціна",
                "ВартістьЗалишку"
            ]
        }

        self.check_sheets()

    # -------------------------------------------------
    # ПЕРЕВІРКА СТРУКТУРИ EXCEL
    # -------------------------------------------------

    def check_sheets(self):

        for sheet_name, headers in self.required_sheets.items():

            if sheet_name not in self.wb.sheetnames:
                raise ValueError(
                    f"Відсутній аркуш: {sheet_name}"
                )

            ws = self.wb[sheet_name]

            actual_headers = [
                ws.cell(row=1, column=i).value
                for i in range(1, len(headers) + 1)
            ]

            if actual_headers != headers:
                raise ValueError(
                    f"Невірна структура аркуша: {sheet_name}\n"
                    f"Очікується: {headers}\n"
                    f"Отримано: {actual_headers}"
                )

    # -------------------------------------------------
    # ОТРИМАННЯ АРКУША
    # -------------------------------------------------

    def get_sheet(self, sheet_name):

        if sheet_name not in self.wb.sheetnames:
            raise ValueError(
                f"Аркуш {sheet_name} не знайдено"
            )

        return self.wb[sheet_name]

    # -------------------------------------------------
    # ПЕРЕВІРКА ЧИСЛОВИХ ЗНАЧЕНЬ
    # -------------------------------------------------

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
    # РОБОТА З ДАТАМИ
    # -------------------------------------------------

    @staticmethod
    def parse_datetime(value):

        if isinstance(value, datetime):
            return value

        if isinstance(value, date):
            return datetime.combine(
                value,
                datetime.min.time()
            )

        if isinstance(value, str):

            value = value.strip()

            formats = [
                "%Y-%m-%d-%H-%M",
                "%Y-%m-%d %H:%M",
                "%Y-%m-%d %H:%M:%S",
                "%d.%m.%Y %H:%M",
                "%d.%m.%Y %H:%M:%S"
            ]

            for fmt in formats:

                try:
                    return datetime.strptime(value, fmt)

                except ValueError:
                    continue

            # Стандартний ISO-формат
            try:
                result = datetime.fromisoformat(value)

                # Excel не підтримує timezone-aware datetime
                if result.tzinfo is not None:
                    result = result.astimezone().replace(
                        tzinfo=None
                    )

                return result

            except ValueError:
                pass

            # Якщо передана тільки дата
            try:
                return datetime.combine(
                    date.fromisoformat(value),
                    datetime.min.time()
                )

            except ValueError:
                pass

        raise ValueError(
            f"Некоректна дата та час: {value}"
        )

    # -------------------------------------------------
    # ЗАВАНТАЖЕННЯ ДОВІДНИКА ТОВАРІВ
    # -------------------------------------------------

    def get_products(self):

        ws = self.get_sheet("Товари")

        products = {}

        for row in ws.iter_rows(
            min_row=2,
            values_only=True
        ):

            code, name, unit = row[:3]

            if code is None:
                continue

            code = str(code).strip()

            if code in products:
                raise ValueError(
                    f"Дубльований код товару: {code}"
                )

            products[code] = {

                "code": code,

                "name": name,

                "unit": unit

            }

        return products

    # -------------------------------------------------
    # ПОШУК ТОВАРУ ЗА КОДОМ
    # -------------------------------------------------

    def get_product(self, code):

        products = self.get_products()

        return products.get(
            str(code).strip()
        )

    # -------------------------------------------------
    # ГЕНЕРАЦІЯ НОМЕРА FIFO-ПАРТІЇ
    # -------------------------------------------------

    def get_next_lot_number(self):

        ws = self.get_sheet("Партії Fifo")

        lot_column = 3

        numbers = []

        for row in range(2, ws.max_row + 1):

            value = ws.cell(
                row,
                lot_column
            ).value

            if isinstance(value, int) and not isinstance(value, bool):
                numbers.append(value)

        return max(numbers, default=0) + 1

    # -------------------------------------------------
    # ДОДАВАННЯ НАДХОДЖЕННЯ
    # -------------------------------------------------

    def add_receipt(
        self,
        code,
        quantity,
        price,
        receipt_date=None
    ):

        # Отримуємо товар із довідника
        product = self.get_product(code)

        if product is None:
            raise ValueError(
                f"Товар з кодом {code} не знайдено"
            )

        # Перевіряємо кількість
        quantity = self.to_decimal(
            quantity,
            "Кількість"
        )

        if quantity <= 0:
            raise ValueError(
                "Кількість повинна бути більшою за 0"
            )

        # Перевіряємо ціну
        price = self.to_decimal(
            price,
            "Ціна"
        )

        if price < 0:
            raise ValueError(
                "Ціна не може бути від'ємною"
            )

        # Поточна дата та час
        if receipt_date is None:
            receipt_date = datetime.now()

        else:
            receipt_date = self.parse_datetime(
                receipt_date
            )

        # Розрахунок загальної вартості
        total = (
            quantity * price
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

        # Отримуємо аркуші
        ws_receipts = self.get_sheet("Надходження")

        ws_fifo = self.get_sheet("Партії Fifo")

        # Генеруємо номер партії
        lot_number = self.get_next_lot_number()

        # Запам'ятовуємо початкову кількість рядків
        receipts_max_row = ws_receipts.max_row

        fifo_max_row = ws_fifo.max_row

        try:

            # Записуємо надходження
            ws_receipts.append([

                receipt_date,

                product["code"],

                product["name"],

                product["unit"],

                float(quantity),

                float(price),

                float(total)

            ])

            # Формат дати та часу
            ws_receipts.cell(
                ws_receipts.max_row,
                1
            ).number_format = "dd.mm.yyyy hh:mm"

            # Створюємо FIFO-партію
            ws_fifo.append([

                receipt_date,

                product["code"],

                lot_number,

                float(quantity),

                float(quantity),

                float(price),

                float(total)

            ])

            # Формат дати та часу
            ws_fifo.cell(
                ws_fifo.max_row,
                1
            ).number_format = "dd.mm.yyyy hh:mm"

            # Зберігаємо Excel
            self.save()

        except Exception:

            # Відновлюємо початкові рядки
            if ws_receipts.max_row > receipts_max_row:

                ws_receipts.delete_rows(
                    receipts_max_row + 1,
                    ws_receipts.max_row - receipts_max_row
                )

            if ws_fifo.max_row > fifo_max_row:

                ws_fifo.delete_rows(
                    fifo_max_row + 1,
                    ws_fifo.max_row - fifo_max_row
                )

            raise

        return {

            "date": receipt_date,

            "code": product["code"],

            "name": product["name"],

            "quantity": quantity,

            "price": price,

            "total": total,

            "lot_number": lot_number

        }

    # -------------------------------------------------
    # ЗБЕРЕЖЕННЯ КНИГИ
    # -------------------------------------------------

    def save(self):

        try:

            self.wb.save(self.file_path)

            print("Excel успішно збережено!")

        except PermissionError:

            raise PermissionError(
                f"Неможливо зберегти файл {self.file_path}.\n"
                "Перевір, чи не відкритий він у Microsoft Excel."
            )

    # -------------------------------------------------
    # ЗАКРИТТЯ КНИГИ
    # -------------------------------------------------

    def close(self):

        self.wb.close()
