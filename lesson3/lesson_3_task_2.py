from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iphon 15 PRO Max", "+78005553535"),
    Smartphone("Google", "Pixel 3", "+78002000600"),
    Smartphone("OnePlus", "OnePlus12", "+79005656789"),
    Smartphone("Samsung", "Samsung Galaxy S24 Ultra", "+79060007654"),
    Smartphone("Realme", "Realme GT 2", "+76548769870") 
]

for x in catalog:
    print("<", x.phone_brand, ">", "-", "<", x.phone_model, ">", ".", "<", x.subscriber_number, ">")

