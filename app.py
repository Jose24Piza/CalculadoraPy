from calculator import Calculator
def main():
    calc = Calculator()
    print("=== CALCULADORA SIMPLE ===")
    print("Operaciones: +, -, *, /")
    try:
        num1 = float(input("Ingrese el primer número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")
        num2 = float(input("Ingrese el segundo número: "))
        if operacion == '+':
            resultado = calc.sum(num1, num2)
        elif operacion == '-':
            resultado = calc.subtract(num1, num2)
        elif operacion == '*':
            resultado = calc.multiply(num1, num2)
        elif operacion == '/':
            resultado = calc.divide(num1, num2)
        else:
            print("Operación no válida")
            return
        print(f"\nResultado: {num1} {operacion} {num2} = {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()