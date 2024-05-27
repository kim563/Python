from mailing import Mailing
from address import Address


home = Address("987654", "Москва", "ул. Ленина", "7", "56")
post = Address("875599", "Павлодар", "ул. Титова", "95", "87")


office = Mailing(post, home, 76, "785467")

print("Отправление <", office.track, "> из <", office.from_address.index,"> , <", office.from_address.city, "> , <", office.from_address.street, ">, <", office.from_address.house, "> - <",  office.from_address.apartment, "> в <", office.to_address.index, ">, <", office.to_address.city, ">, <", office.to_address.street,">, <", office.to_address.house, "> -<", office.to_address.apartment, ">. Стоимость", office.cost, "рублей.")
