def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += '_'
            snake_case += char.lower()
        else:
            snake_case += char
    return snake_case

def main():
    camel_case = input("camelCase: ")
    snake_case = camel_to_snake(camel_case)
    print("snake_case:",snake_case)

if __name__ == "__main__":
    main()