"""
Tests de integración para la CalculadoraPy
Verifica la integración entre componentes
"""

import pytest
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculadora import Calculator
import app


class TestIntegracion:
    """Pruebas de integración entre módulos"""
    
    def setup_method(self):
        """Configurar entorno de prueba"""
        self.calc = Calculator()
        
    def test_calculadora_importada_correctamente(self):
        """Verificar que la calculadora se importa correctamente en app.py"""
        assert hasattr(app, 'calc')
        assert isinstance(app.calc, Calculator)
    
    def test_app_flask_configurado(self):
        """Verificar que la aplicación Flask está configurada"""
        assert hasattr(app, 'app')
        assert app.app.config['ENV'] == 'production'
    
    def test_operaciones_completas(self):
        """Probar secuencia completa de operaciones"""
        # Suma
        resultado = self.calc.sum(15, 30)
        assert resultado == 45
        
        # Resta
        resultado = self.calc.subtract(100, 45)
        assert resultado == 55
        
        # Multiplicación
        resultado = self.calc.multiply(6, 7)
        assert resultado == 42
        
        # División
        resultado = self.calc.divide(144, 12)
        assert resultado == 12
    
    def test_manejo_errores(self):
        """Verificar manejo de errores"""
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            self.calc.divide(10, 0)
    
    def test_app_rutas(self):
        """Verificar que las rutas de la app existen"""
        from flask import Flask
        assert hasattr(app, 'home')
        assert hasattr(app, 'health')
        assert hasattr(app, 'calcular')
    
    def test_health_check(self):
        """Probar el endpoint de health check"""
        # Simular petición al endpoint /health
        with app.app.test_client() as client:
            response = client.get('/health')
            assert response.status_code == 200
            data = response.get_json()
            assert 'status' in data
            assert data['status'] == 'healthy'
            assert 'timestamp' in data