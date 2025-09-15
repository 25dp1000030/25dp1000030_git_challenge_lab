from add import add
def main():
    print("Arithmetic Operations")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Sum: {add(a, b)}")

if __name__ == "__main__":
    main()