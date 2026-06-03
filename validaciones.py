def es_stock_valido(stock: str):
    return stock.isnumeric()


def pedir_stock():
    stock = input('Escribe un stock: ')
    if not es_stock_valido(stock):
        print(f'ERROR! {stock} no es un stock valido')
        return pedir_stock()
    return int(stock)

