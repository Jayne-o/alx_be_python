class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(cls.calculation_type)
        return a * b

  from class_static_methods_demo import Calculator

def main():
    # Static method call
    result_add = Calculator.add(10, 5)
    print(f"Addition Result: {result_add}")

    # Class method call
    result_multiply = Calculator.multiply(10, 5)
    print(f"Multiplication Result: {result_multiply}")

if __name__ == "__main__":
    main()
