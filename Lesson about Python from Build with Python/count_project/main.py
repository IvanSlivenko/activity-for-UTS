
from database.excel_manager import ExcelManager
from services.expense_service import ExpenseService
from datetime import datetime



# region ----------------------------------------------------------- var 1 products = excel.get_products()
# def main():


#     excel = ExcelManager("db.xlsx")

#     print("Excel підключено успішно!")

#     products = excel.get_products()

#     print(f"Кількість товарів: {len(products)}")

#     for code, product in products.items():

#         print(
#             code,
#             product["name"],
#             product["unit"]
#         )

#     excel.close()
# endregion

# region ----------------------------------------------------------- var 2 # Пошук за кодом product = excel.get_product("1")
# def main():

#     excel = ExcelManager("db.xlsx")

#     # Пошук за кодом
#     product = excel.get_product("1")

#     print("\nПошук товару:")

#     if product:
#         print(product)
#     else:
#         print("Товар не знайдено")

#     excel.close()    

# if __name__ == "__main__":
#     main()
# endregion

# region ----------------------------------------------------------- var 3 excel.add_receipt

# def main():

#     excel = ExcelManager("db.xlsx")

#     try:

#         result = excel.add_receipt(
#             code="1",
#             quantity=10,
#             price=800

#         )

#         print("\nНадходження успішно зареєстровано!")
#         print("-" * 40)

#         print(f"Товар: {result['name']}")
#         print(f"Кількість: {result['quantity']}")
#         print(f"Ціна: {result['price']} грн")
#         print(f"Загальна вартість: {result['total']} грн")
#         print(f"Номер партії: {result['lot_number']}")

#         print("-" * 40)

#     finally:
#         excel.close()


# if __name__ == "__main__":
#     main()

# endregion

# region ----------------------------------------------------------- var 4 expense.write_off

def main():

    excel = ExcelManager("db.xlsx")

    try:

        expense = ExpenseService(excel)

        result = expense.write_off(          
            code="1",
            quantity=15

        )

        print("\nСписання успішно зареєстровано!")
        print("-" * 45)

        print(f"Товар: {result['name']}")
        print(f"Кількість: {result['quantity']}")
        print(f"Загальна вартість: {result['total_value']} грн")

        print("\nРозподіл за партіями:")

        for item in result["allocations"]:

            print(
                f"Партія №{item['lot']} | "
                f"Кількість: {item['quantity']} | "
                f"Ціна: {item['price']} | "
                f"Вартість: {item['value']} грн"
            )

        print("-" * 45)

    finally:
        excel.close()


if __name__ == "__main__":
    main()

# endregion    
