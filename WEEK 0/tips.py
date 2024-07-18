def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d.lstrip('$')) #使用 lstrip 删除左侧的$

def percent_to_float(p):
    return float(p.rstrip('%')) / 100  #使用 rstrip 删除右侧的%

main()
