def bank(x, y):
    summa_vklada = x
    for n in range(1, y):
        summa_vklada = summa_vklada + summa_vklada * 0.1
    return summa_vklada

print(bank(100000, 12))