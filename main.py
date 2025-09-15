from add import add
from sub import subtract

def main():
    print("Arithmetic Operations")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Sum: {add(a, b)}")
    print(f"Difference: {subtract(a, b)}")
if __name__ == "__main__":
    main()