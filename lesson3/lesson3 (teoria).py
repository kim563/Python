from lesson3.user_teoria import User
from lesson3.card_teoria import Card

Alex = User("Alex")


Alex.sayName()
Alex.sayAge()
Alex.setAge(33)
Alex.sayAge()

card = Card("5456 7658 6578 7865", "11/28", "Alex F")

Alex.addCard(card)
Alex.getCard().pay(1000)


