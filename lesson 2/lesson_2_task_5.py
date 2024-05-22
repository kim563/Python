def month_to_season(mes):
    if mes > 2 and mes < 6:
        print("Весна")
    elif mes > 5 and mes < 9:
        print("Лето")
    elif mes > 8 and mes < 12:
        print("Осень")
    elif mes > 0 and mes < 3 or mes == 12:
        print("Зима")
    else:
        print ("Такого месяца нет!")

month_to_season(5)