

def versandkosten(*prices: float):
    sum_prices = sum(prices)
    if sum_prices > 50:
        return sum_prices
    return sum_prices + 8.5


def endpreis(discount: float, *prices: float):
    discounted_price = sum(prices) * (1 - discount / 100)
    return round(versandkosten(discounted_price),2)

class OnlineShop:

    def __init__(self, name: str, branche: str, ort: str):
        self.name = name
        self.branche = branche
        self.ort = ort
        self.produkte: dict = {}

    def __str__(self):
        return f"Name: {self.name}, Branche: {self.branche}, Ort: {self.ort}, \nProdukte: {self.produkte}" 

    def add_product(self, product: str, price: float):
        self.produkte[product] = price

    def bestellung(self, order: dict):
        sum_order = 0
        for product_name, count in order.items():
            if product_name not in self.produkte:
                print(f"Leider ist {product_name} nicht im Shop verfügbar. Bestellung abgebrochen!")
                return

            sum_order += self.produkte[product_name] * count

        print(sum_order)
