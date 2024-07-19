total = 0
while total < 50:
    insert = int(input("Insert Coin: "))
    if insert in [5, 10, 25]:
        total += insert
    if total >= 50:
        print("Change Owed:", total - 50)
    else:
        print("Amount Due:", 50 - total)


