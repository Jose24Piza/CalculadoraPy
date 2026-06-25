#!/bin/bash
# ============================================
# Script: Despliegue a Producción
# ============================================

set -e

VERSION=$1

if [ -z "$VERSION" ]; then
    echo "❌ Error: Versión no especificada"
    echo "Uso: ./deploy-production.sh <version>"
    exit 1
fi

echo "═══════════════════════════════════════"
echo "🚀 DESPLIEGUE A PRODUCCIÓN"
echo "═══════════════════════════════════════"
echo "⚠️  ADVERTENCIA: Este es el entorno de PRODUCCIÓN"
echo "📌 Versión: $VERSION"
echo "⏰ Fecha: $(date)"
echo "═══════════════════════════════════════"

# Solicitar confirmación
read -p "¿Estás seguro de desplegar a PRODUCCIÓN? (yes/no): " CONFIRM
if [ "$CONFIRM" != "yes" ]; then
    echo "❌ Despliegue cancelado por el usuario"
    exit 1
fi

# Variables
PRODUCTION_DIR="deployment-artifacts"
LOG_FILE="logs/deploy-production-$(date +%Y%m%d).log"
BACKUP_DIR="backups/production-$(date +%Y%m%d-%H%M%S)"

# Crear directorios
mkdir -p logs backups

# Función para loggear
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# 1. Crear backup
log "📦 Creando backup de producción actual..."
mkdir -p "$BACKUP_DIR"
if [ -d "$PRODUCTION_DIR" ]; then
    cp -r "$PRODUCTION_DIR"/*