import json
import random


class Vendor:

    def __init__(self, *products):
        self.__total_balance = 0
        self.balance = 0
        self.shop = []

        if len(products) < 3:
            raise AssertionError(f"The least of products is 3, what you have is {len(products)} product")
        else:
            for product in products:
                self.shop.append(product)

    def __str__(self):
        return f"Vendor {random.randint(1, 10)}"

    def __repr__(self):
        return f"Vendor {random.randint(1, 10)}"

    def __len__(self):
        return len(self.shop)

    def add_product(self, product):
        if isinstance(product, dict):
            self.shop.append(product)
            print(f"{product} has been added")
        else:
            print("Not the right product")

    def insert_coin(self, coin):
        # Identify the coin in the vending machine is correct.
        self.balance += float(coin)
        print(f"Balance: {self.balance}")
        return self.balance

    def display_product(self):
        print("\n List of Product \n")

        for product in self.shop:
            if product["stock"] == 0:
                self.shop.remove(product)

        for product in self.shop:
            print(f"Name: {product['name']}. Price: {product['price']}. Stock: {product['stock']}")

        print("-----------------------------------------------------------------")

    def get_product(self, item):
        for product in self.shop:
            if product['name'] == item:
                print("Product is available")

                if float(self.balance) < float(product["price"]):
                    print("You can't buy this product. Insert more coins.")
                    break
                else:
                    self.balance -= float(product["price"])
                    print(f'You got {product["name"]}. Balance change: {self.balance}')
                    print("-------------------------------------------------")
                    break
            else:
                print("Product is not available")
                break
        print("----------------------------------------------")

    def collect_change(self):
        if self.balance > 0:
            print(f"Balance change: {self.balance}")


def run_vendor():
    with open('pro.json', 'r') as f:
        products = json.load(f)

    vender = Vendor(*products["products"])

    print("-----------------------------------")
    print("Welcome!")

    running = True

    while running:
        vender.display_product()
        selected_product = input('Product Name: ')

        print("-----------------------------------------")
        selected_coin = input('Insert coin: ')
        # vender.balance = float(selected_coin)
        vender.balance = float(vender.insert_coin(selected_coin))

        vender.get_product(selected_product)

        if input("You want to buy again. yes or no: ") == 'no':
            running = False
            vender.collect_change()
        else:
            continue


print(run_vendor())
