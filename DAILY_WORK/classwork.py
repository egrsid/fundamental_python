import qrcode
import json
import os

products = [
    {
        'product_name': 'Батон',
        'product_type': 'Хлеб',
        'manufacture_date': '2023-10-01',
        'expiry_date': '2023-10-08',
        'quantity': 0.5,
        'unit': 'кг',
        "nutrition_info": {'calories': 250, 'proteins': 5, 'fats': 3, 'carbohydrates': 45},
        'measurement_type': 'вес'
    },
    {
        'product_name': 'Молоко',
        'product_type': 'Напиток',
        'manufacture_date': '2023-10-02',
        'expiry_date': '2023-10-07',
        'quantity': 1,
        'unit': 'литр',
        'nutrition_info': {'calories': 70, 'proteins': 3, 'fats': 4, 'carbohydrates': 5},
        'measurement_type': 'объем'
    },
    # Дополнительные примеры продуктов
    {
        'product_name': 'Яблоко',
        'product_type': 'Фрукт',
        'manufacture_date': '2023-10-03',
        'expiry_date': '2023-10-13',
        'quantity': 2,
        'unit': 'кг',
        'nutrition_info': {'calories': 52, 'proteins': 0.26, 'fats': 0.17, 'carbohydrates': 14},
        'measurement_type': 'вес'
    },
    {
        'product_name': 'Творог',
        'product_type': 'Молочные продукты',
        'manufacture_date': '2023-10-04',
        'expiry_date': '2023-10-11',
        'quantity': 0.2,
        'unit': 'кг',
        'nutrition_info': {'calories': 86, 'proteins': 12, 'fats': 5, 'carbohydrates': 3},
        'measurement_type': 'вес'
    },
    {
        'product_name': 'Оливковое масло',
        'product_type': 'Масло',
        'manufacture_date': '2023-10-05',
        'expiry_date': '2023-10-25',
        'quantity': 0.75,
        'unit': 'литр',
        'nutrition_info': {'calories': 884, 'proteins': 0, 'fats': 100, 'carbohydrates': 0},
        'measurement_type': 'объем'
    }]
names = ['Loaf', 'Milk', 'Apple', 'Curd', 'Olive oil']

# Создать директорию для QR-кодов, если она не существует
if not os.path.exists(r"C:\projects\Python\fundamental_python\DATA_BASES\qr_codes"):
    os.makedirs(r"C:\projects\Python\fundamental_python\DATA_BASES\qr_codes")


# Генерация QR-кодов
for prod, n in zip(products, names):

    # Преобразовать словарь в JSON-строку
    product_json = json.dumps(prod, ensure_ascii=False)

    # Создать QR-код
    qr = qrcode.make(product_json)

    # Создать имя файла из переведенного названия
    # Заменить пробелы на подчеркивания и добавить расширение .png
    file_name = fr"C:\projects\Python\fundamental_python\DATA_BASES\qr_codes/{n.replace(' ', '_')}.png"

    # Сохранить QR-код в файл
    qr.save(file_name)