dict = {}
while True:
    try:
        item = input().upper()
    except EOFError:
        print("")
        break

    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1

for item in sorted(dict.keys()):
    print(f"{dict[item]} {item}")
