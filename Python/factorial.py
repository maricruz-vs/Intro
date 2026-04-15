def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    print("Factorial Calculator")
    try:
        value = input("Enter a non-negative integer: ")
        number = int(value)
        if number < 0:
            raise ValueError("Input must be a non-negative integer")
        print(f"{number}! = {factorial(number)}")
    except ValueError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
