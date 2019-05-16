
class Order:

    def __init__(self, number, shipping_method, datetime, name):
        self.items = {}
        self.quantities = {}
        self.picked = {}
        self.total = 0
        self.picked_total = 0

        self.number = number
        self.shipping_method = shipping_method
        self.datetime = datetime
        self.name = name

    def add_meals(self, sku, meal, quantity):

        if sku in self.items:
            self.quantities[sku] += int(quantity)
            self.total += int(quantity)
        else:
            self.items[sku] = meal
            self.quantities[sku] = int(quantity)
            self.picked[sku] = 0
            self.total += int(quantity)

    def order_contains_sku(self, sku):
        if sku in self.items:
            return True
        else:
            return False


    def get_stuff(self):
        print(str(self.name) + " ordered " + str(self.total) + " meals with " + str(len(self.quantities)) + " options.")

    def meal_scanned(self, sku):
        self.picked[sku] += 1
        self.picked_total += 1
        print(str(self.total - self.picked_total) + " meals remaining")

    def get_quantities(self):
        return self.quantities

    def get_picked(self):
        return self.picked