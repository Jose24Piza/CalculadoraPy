"""
Tests de API para la CalculadoraPy
Prueba los endpoints HTTP de la aplicación
"""

import pytest
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import app


class TestAPI:
    """Pruebas de los endpoints de la API"""
    
    def setup_method(self):
        """Configurar cliente de prueba"""
        self.client = app.app.test_client()
    
    def test_home_endpoint(self):
        """Probar el endpoint raíz /"""
        response = self.client.get('/')
        assert response.status_code == 200
        assert b'CalculadoraPy en Render' in response.data
    
    def test_health_endpoint(self):
        """Probar el endpoint /health"""
        response = self.client.get('/health')
        assert response.status_code == 200
        data = response.get_json()
        assert data['status'] == 'healthy'
        assert 'cpu' in data
        assert 'memory' in data
    
    def test_calcular_suma(self):
        """Probar operación de suma via API"""
        response = self.client.get('/calcular/%2B/5/3')
        assert response.status_code == 200
        data = response.get_json()
        assert data['resultado'] == 8
        assert data['operacion'] == '+'
    
    def test_calcular_resta(self):
        """Probar operación de resta via API"""
        response = self.client.get('/calcular/-/10/4')
        assert response.status_code == 200
        data = response.get_json()
        assert data['resultado'] == 6
    
    def test_calcular_multiplicacion(self):
        """Probar operación de multiplicación via API"""
        response = self.client.get('/calcular/*/6/7')
        assert response.status_code == 200
        data = response.get_json()
        assert data['resultado'] == 42
    
    def test_calcular_division(self):
        """Probar operación de división via API"""
        response = self.client.get('/calcular//15/3')
        assert response.status_code == 200
        data = response.get_json()
        assert data['resultado'] == 5
    
    def test_calcular_division_cero(self):
        """Probar división por cero via API"""
        response = self.client.get('/calcular//10/0')
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data
        assert 'No se puede dividir por cero' in data['error']
    
    def test_calcular_operacion_invalida(self):
        """Probar operación inválida via API"""
        response = self.client.get('/calcular/%25/5/3')  # %25 = %
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data
        assert 'Operación no válida' in data['error']