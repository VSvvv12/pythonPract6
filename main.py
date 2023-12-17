from app import calculator

def main():
    result = calculator.Calculator(3, 6)
    return result.arithmetic()


if __name__ == '__main__':

    print(main())
