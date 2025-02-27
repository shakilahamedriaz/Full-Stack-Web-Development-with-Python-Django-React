# Product - name, price, stock
# Customer - name
# CartItems - product, quantity
# Cart - User, CartItems
# Payment - (Paypal, Credit Card)



# 1. Create Product Class
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def __str__(self):
        return f"{self.name}-${self.price}-{self.stock}"


class Customer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class CartItems:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity


class Cart:
    def __init__(self, customer):
        self.customer = customer
        self.cart = []
    
    def add_to_cart(self, product, quantity):
        self.cart.append(CartItems(product, quantity))
    
    def calculate_total(self):
        total_price = 0

        for item in self.cart:
            total_price += item.get_total_price()

        return total_price
    
    def display_cart(self):
        print(f"shopping cart of {self.customer}")
        for item in self.cart:
            print(f"{item.product.name} * {item.quantity} - ${item.get_total_price()}")
        print(f"Total: $ {self.calculate_total()}")





laptop = Product('laptop', 10000, 10)
phone = Product('Iphone', 20000, 20)

abdur = Customer('Abdur')
abdur_cart = Cart(abdur)

abdur_cart.add_to_cart(laptop, 2)
abdur_cart.add_to_cart(phone, 1)

abdur_cart.display_cart()


# print(abdur)

# print(laptop)
# print(phone)




