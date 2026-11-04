import week1.online_shop as os

assert os.endpreis(10, 12, 18, 22) == 55.3
print(os.endpreis(10, 12, 18, 22))

assert os.endpreis(0, 5, 11, 3) == 27.5
print(os.endpreis(0, 5, 11, 3))

assert os.endpreis(100, 1442, 32, 82) == 8.5
print(os.endpreis(100, 1442, 32, 82))



online_shop = os.OnlineShop("testname", "testBranche", "testOrt")
online_shop.add_product("testProdukt", 19.99)
online_shop.add_product("testProdukt2", 12.19)
online_shop.add_product("testProdukt3", 0.50)
print(str(online_shop))
online_shop.bestellung({"testProdukt": 3,"testProdukt2": 1,"testProdukt3": 4})
online_shop.bestellung({"testProdukt": 3,"testProdukt2": 2,"testProdukt3": 4,"testProdukt4": 9})