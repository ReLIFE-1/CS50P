# 转换函数
def convert(text):
    text = text.replace(":)","🙂").replace(":(","🙁")
    return text

# 主函数
def main():
    print(convert(input()))

if __name__ == "__main__":
    main()