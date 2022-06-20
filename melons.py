class MelonOrder:
    def get_base_price(self):
        return 5.0

class WatermelonOrder(MelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Fall", "Summer"]

    def get_price(self, qty):

        total = self.get_base_price() * qty
        if qty >= 5:
            total = total * 0.75
        return total


class CantaloupeOrder(MelonOrder):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):

        total = self.get_base_price() * qty
        return total


class CasabaOrder(MelonOrder):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Spring", "Summer", "Fall", "Winter"]

    def get_price(self, qty):

        total = self.get_base_price() * qty
        return total


class SharlynOrder(MelonOrder):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        
        total = self.get_base_price() * qty
        return total

class SantaClausOrder(MelonOrder):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Spring", "Winter"]

    def get_price(self, qty):

        total = self.get_base_price() * qty
        return total
        

class ChristmasOrder(MelonOrder):
    species = "Christmas"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Winter"]

    def get_price(self, qty):

        total = self.get_base_price() * qty
        return total


class HornedMelonOrder(MelonOrder):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):

        total = self.get_base_price() * qty
        return total


class XiguaOrder(MelonOrder):
    species = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Summer"]

    def get_price(self, qty):

        total = self.get_base_price() * qty
        return total


class OgenOrder(MelonOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):

        total = self.get_base_price() * qty
        return total
