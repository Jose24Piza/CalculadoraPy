from flask import Flask, jsonify
from calculadora import Calculator
import psutil
import time

# ============ CREAR LA APLICACIÓN FLASK A NIVEL GLOBAL ============
app = Flask(__name__)
calc = Calculator()

# ============ RUTAS DE LA API ============
@app.route('/')
def home():
    return "CalculadoraPy en Render 🚀"

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time(),
        'memory': psutil.virtual_memory().percent,
        'cpu': psutil.cpu_percent()
    })

@app.route('/calcular/<operacion>/<float:num1>/<float:num2>')
def calcular(operacion, num1, num2):
    """API REST para calcular operaciones: /calcular/+/-/*/5/3"""
    try:
        if operacion == '+':
            resultado = calc.sum(num1, num2)
        elif operacion == '-':
            resultado = calc.subtract(num1, num2)
        elif operacion == '*':
            resultado = calc.multiply(num1, num2)
        elif operacion == '/':
            resultado = calc.divide(num1, num2)
        else:
            return jsonify({'error': 'Operación no válida'}), 400
        
        return jsonify({
            'operacion': operacion,
            'num1': num1,
            'num2': num2,
            'resultado': resultado
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Error inesperado: {e}'}), 500

# ============ FUNCIÓN PRINCIPAL (CONSOLA) ============
def main():
    """Interfaz de consola para usar la calculadora"""
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
    # Si se ejecuta directamente, corre la consola
    # Para ejecutar la API: gunicorn app:app
    main()