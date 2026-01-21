def atm_change(n):
    so50 = n // 50
    n = n % 50 

    so20 = n // 20
    n = n % 20

    so1 = n
    return f"{so50}{so20}{so1}"
n = int(input())
print(atm_change(n))