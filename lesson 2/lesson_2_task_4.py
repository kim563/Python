def fizz_buzz(n):
    for x in range(1, n):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBizz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Bizz")
        else: 
            print(x)
 
fizz_buzz(19)