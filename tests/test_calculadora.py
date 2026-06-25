import pytest
from calculadora import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()
    
    def test_suma(self):
        assert self.calc.sum(2, 3) == 5
    
    def test_resta(self):
        assert self.calc.subtract(10, 5) == 5
    
    def test_multiplicacion(self):
        assert self.calc.multiply(3, 4) == 12
    
    def test_division(self):
        assert self.calc.divide(10, 2) == 5
    
    def test_division_cero(self):
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            self.calc.divide(5, 0)
    
    def test_integracion_app(self):
        """Test de integración: verifica que app.py importe correctamente"""
        import app
        assert hasattr(app, 'app')
        assert callable(app.app)  # Flask app es callable