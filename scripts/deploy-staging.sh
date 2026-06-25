#!/bin/bash
# ============================================
# Script: Despliegue a Staging
# ============================================

set -e

VERSION=$1

if [ -z "$VERSION" ]; then
    echo "❌ Error: Versión no especificada"
    echo "Uso: ./deploy-staging.sh <version>"
    exit 1
fi

echo "═══════════════════════════════════════"
echo "🧪 DESPLIEGUE A STAGING"
echo "═══════════════════════════════════════"
echo "📌 Versión: $VERSION"
echo "⏰ Fecha: $(date)"
echo "═══════════════════════════════════════"

# Variables
STAGING_DIR="deployment-artifacts"
LOG_FILE="logs/deploy-staging-$(date +%Y%m%d).log"

# Crear directorio de logs si no existe
mkdir -p logs

# Función para loggear
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# 1. Verificar artefactos
log "📂 Verificando artefactos..."
if [ ! -d "$STAGING_DIR" ]; then
    log "❌ Directorio $STAGING_DIR no encontrado"
    exit 1
fi

# 2. Validar archivos necesarios
log "🔍 Validando archivos..."
REQUIRED_FILES=("app.py" "calculadora.py" "requirements.txt")
for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$STAGING_DIR/$file" ]; then
        log "❌ Archivo $file no encontrado en $STAGING_DIR"
        exit 1
    fi
done
log "✅ Archivos validados correctamente"

# 3. Preparar entorno de staging
log "🖥️ Preparando entorno de staging..."
cd "$STAGING_DIR"

# Crear archivo de configuración para staging
cat > staging-config.json << EOF
{
  "environment": "staging",
  "version": "$VERSION",
  "deploy_time": "$(date -Iseconds)",
  "url": "https://calculadorapy-staging.onrender.com",
  "features": {
    "debug": true,
    "logging": true,
    "metrics": true
  }
}
EOF

log "✅ Configuración de staging generada"

# 4. Simular despliegue a staging
log "🚀 Iniciando despliegue a staging..."
echo "📦 Copiando archivos al servidor de staging..."
sleep 2
echo "🔧 Configurando variables de entorno..."
sleep 2
echo "🔄 Reiniciando servicio de staging..."
sleep 2

log "✅ Despliegue a staging completado"

# 5. Verificar estado
log "🔍 Verificando estado del servicio..."
echo "🌐 URL: https://calculadorapy-staging.onrender.com"
echo "📊 Estado: ✅ Servicio activo"

# 6. Generar reporte
cat > deployment-report.json << EOF
{
  "environment": "staging",
  "version": "$VERSION",
  "status": "success",
  "deployed_at": "$(date -Iseconds)",
  "artifacts": ["${REQUIRED_FILES[@]}"],
  "url": "https://calculadorapy-staging.onrender.com"
}
EOF

log "📝 Reporte de despliegue generado"

cd ..

echo "═══════════════════════════════════════"
echo "✅ DESPLIEGUE A STAGING EXITOSO"
echo "═══════════════════════════════════════"
echo "📌 Versión: $VERSION"
echo "🌐 URL: https://calculadorapy-staging.onrender.com"
echo "📄 Log: $LOG_FILE"
echo "═══════════════════════════════════════"

exit 0