from smartphone import Smartphone

catalog = [
    Smartphone('Apple', 'iPhone 15', '+79233212552'),
    Smartphone('Samsung', 'Galaxy S24', '+79055682673'),
    Smartphone('POCO', 'X6', '+79098994560'),
    Smartphone('Xiaomi', '13T Pro', '+79526664433'),
    Smartphone('Honor', '400 Pro', '+79994563211')
]

for i in catalog:
    print(f'{i.br} - {i.mo}. {i.nu}')