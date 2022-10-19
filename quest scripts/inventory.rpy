init python:
    from collections import OrderedDict


    class Item:
        def __init__(self, name, image):
            self.name = name
            self.image = image


    class Container:
        # Can handle any amount of item
        # Can handle only max_item_types item types
        def __init__(self):
            # item: amount
            self.inventory = OrderedDict()
            self.max_item_types = 12

        def add(self, item, amount):
            if len(self.inventory) < self.max_item_types or item in self.inventory:
                self.inventory[item] = self.inventory.get(item, 0) + amount


        def remove(self, item, amount):
            """
            Remove specified amount of item from inventory. If remaining amount of item == 0
            also deletes item from inventory dict
            Safe for work if you check whether those amount of items is stored
            in inventory before usage

            :param Item item: Inventory item
            :param int amount: how many copies of item should be removed
            :return: None
            """
            # Decrease amount of item
            if item in self.inventory:
                self.inventory[item] -= amount

                # Remove item from the dict if it's amount is 0 or less
                if self.inventory[item] <= 0:
                    del self.inventory[item]


        def get_amount(self, item):
            return self.inventory.get(item, 0)


        def can_take(self, item, amount):
            # TODO we can rewrite checks in game from get_amount() == , to can_take
            if self.inventory[item] >= amount:
                return True
            return False
