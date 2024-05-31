from test.calculitor_test import calculitor


calkul = calculitor()

def test_sum_positiv_nums():
    calkul = calculitor()
    res = calkul.sum(4, 5)
    assert res == 9

    
def test_sum_negativ_nums():
    calkul = calculitor()
    res = calkul.sum(-6, -10)
    assert res == -16


def test_sum_positiv_and_negativ_nums():
    calkul = calculitor()
    res = calkul.sum(4, 5)
    assert res == 9
    

    

# print("start")
# res = calkul.sum(4, 5)
# assert res == 9

# res = calkul.sum(-5, -10)
# assert res == -15

# res = calkul.sum(-6, 6)
# assert res == 0

# res = calkul.sum(5.6, 4.3)
# res = round(res, 1)
# print(res)
# assert res == 9.9

# res = calkul.sum(10, 0)
# assert res == 10

# numbers = []
# res = calkul.avg(numbers)
# assert res == 0

# numbers = [1,2,3,4,5,6,7,8,9,5]
# res = calkul.avg(numbers)
# print(res)
# assert res == 5

# res = calkul.div(10, 0)
# assert res == None

# print("finish")

