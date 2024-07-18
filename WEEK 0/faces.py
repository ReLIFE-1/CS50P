# 转换函数
def convert(text):
    text = text.replace(":)","🙂").replace(":(","🙁")
    return text

# 主函数
def main():
    print(convert(input()))

main()