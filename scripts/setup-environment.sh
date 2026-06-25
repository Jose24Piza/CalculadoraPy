#!/bin/bash
# ============================================
# Script: Generación del Entorno de Liberación
# ============================================

set -e  # Detener en caso de error

echo "═══════════════════════════════════════"
echo "🖥️ GENERANDO ENTORNO DE LIBERACIÓN"
echo "═══════════════════════════════════════"

# Variables de entorno
PYTHON_VERSION="3.11"
VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"

# 1. Verificar Python
echo "🔍 Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python no está instalado"
    exit 1
fi

PYTHON_VERSION_INSTALLED=$(python3 --version | cut -d' ' -f2)
echo "✅ Python $PYTHON_VERSION_INSTALLED detectado"

# 2. Crear entorno virtual
echo "📦 Creando entorno virtual..."
if [ -d "$VENV_DIR" ]; then
    echo "⚠️ El entorno virtual ya existe. Eliminando..."
    rm -rf "$VENV_DIR"
fi

python3 -m venv "$VENV_DIR"
echo "✅ Entorno virtual creado en $VENV_DIR"

# 3. Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source "$VENV_DIR/bin/activate"

# 4. Instalar dependencias
echo "📦 Instalando dependencias..."
if [ -f "$REQUIREMENTS_FILE" ]; then
    pip install --upgrade pip
    pip install -r "$REQUIREMENTS_FILE"
    pip install flake8 mypy pytest pytest-cov
    echo "✅ Dependencias instaladas"
else
    echo "❌ Archivo $REQUIREMENTS_FILE no encontrado"
    exit 1
fi

# 5. Verificar instalación
echo "🔍 Verificando instalación..."
python -c "import flask; print('✅ Flask instalado')"
python -c "import pytest; print('✅ Pytest instalado')"

# 6. Generar archivo de entorno
cat > .env << EOF
# Entorno de liberación generado automáticamente
PYTHON_VERSION=$PYTHON_VERSION
VENV_DIR=$VENV_DIR
FLASK_ENV=development
DATABASE_URL=sqlite:///app.db
EOF

echo "✅ Archivo .env generado"

# 7. Crear directorios necesarios
mkdir -p logs
mkdir -p data
mkdir -p reports

echo "✅ Directorios creados: logs, data, reports"

# 8. Resumen final
echo "═══════════════════════════════════════"
echo "✅ ENTORNO GENERADO CORRECTAMENTE"
echo "═══════════════════════════════════════"
echo "🐍 Python: $(python --version)"
echo "📦 Pip: $(pip --version)"
echo "📁 Directorio: $(pwd)"
echo "📂 Venv: $VENV_DIR"
echo "📋 Requirements: $(wc -l < $REQUIREMENTS_FILE) paquetes"
echo "═══════════════════════════════════════"

# Desactivar entorno virtual
deactivate

exit 0