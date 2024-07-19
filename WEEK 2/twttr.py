s = input("Input: ")
ans = ""
for char in s:
    if char not in "aoeiuAOEIU":
        ans += char
print("Output:",ans)