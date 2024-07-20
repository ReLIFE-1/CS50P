def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6: #长度小于2或者大于6
        return False
    if not s[0:2].isalpha(): #前两个不是字母
        return False
    if not s.isalnum(): #s不是字母或数字
        return False
    
    flag = False
    for char in s:
        if char.isdigit():
            if char == '0' and not flag: #char是0并且前面是字母
                return False        
            flag = True
        if char.isalpha() and flag: #char是字母并且前面是数字
            return False
    
    return True



main()