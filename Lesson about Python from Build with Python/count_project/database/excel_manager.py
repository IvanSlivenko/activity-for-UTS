
from pathlib import Path
from openpyxl import load_workbook


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
                "Ціна за 1",
                "Вартість"
            ],
            "Видаток": [
                "Дата",
                "Код",
                "Назва",
                "Одиниця виміру",
                "Кількість",
                "Ціна списання",
                "Вартість"
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
                "НомерПартії",
                "Код товару",
                "ПочатковаКількість",
                "Кількість залишку",
                "Ціна"
            ]
        }

        self.check_sheets()

    # Перевірка аркушів
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

    # Отримання аркуша
    def get_sheet(self, sheet_name):

        if sheet_name not in self.wb.sheetnames:
            raise ValueError(
                f"Аркуш {sheet_name} не знайдено"
            )

        return self.wb[sheet_name]

    # Завантаження довідника товарів
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

    # Пошук товару за кодом
    def get_product(self, code):

        products = self.get_products()

        return products.get(str(code).strip())

    # Збереження книги
    def save(self):

        self.wb.save(self.file_path)

    # Закриття книги
    def close(self):

        self.wb.close()
