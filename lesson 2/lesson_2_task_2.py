def is_year_leap(got):
    if got % 4 == 0:
        return True 
    else: 
        return False  


out2024 = is_year_leap(2024)
out2023 = is_year_leap(2023)

print("Год 2024:" + str(out2024))
print("Год 2023:" + str(out2023))