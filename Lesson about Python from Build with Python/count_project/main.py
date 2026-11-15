
from database.excel_manager import ExcelManager


def main():

    excel = ExcelManager("db.xlsx")

    print("Excel підключено успішно!")

    products = excel.get_products()

    print(f"Кількість товарів: {len(products)}")

    for code, product in products.items():

        print(
            code,
            product["name"],
            product["unit"]
        )

    excel.close()


if __name__ == "__main__":
    main()
