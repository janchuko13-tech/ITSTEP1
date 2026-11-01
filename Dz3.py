
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product.quantity > 0:
            self.products.append(product)
            product.quantity -= 1
            print(f"{product.name} додано до кошика")
        else:
            print(f"{product.name} немає в наявності")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            product.quantity += 1
            print(f"{product.name} видалено з кошика")
        else:
            print("Товару немає в кошику")

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_cart(self):
        print("Ваш кошик:")
        for product in self.products:
            print(product.name, "-", product.price, "грн")
        print("Загальна вартість:", self.total_price(), "грн")


phone = Product("Телефон", 10000, 5)
laptop = Product("Ноутбук", 25000, 3)
mouse = Product("Мишка", 500, 10)

cart = Cart()

cart.add_product(phone)
cart.add_product(laptop)
cart.add_product(mouse)

cart.show_cart()

cart.remove_product(mouse)

cart.show_cart()
