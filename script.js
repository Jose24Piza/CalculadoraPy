// script.js
document.addEventListener('DOMContentLoaded', function() {
    // Actualizar timestamp
    const now = new Date();
    const timestampElement = document.getElementById('timestamp');
    const loadTimeElement = document.getElementById('loadTime');
    const buildNumberElement = document.getElementById('buildNumber');
    const progressFill = document.getElementById('progressFill');
    const progressLabel = document.getElementById('progressLabel');
    
    if (timestampElement) {
        timestampElement.textContent = now.toLocaleString('es-ES');
    }
    
    if (loadTimeElement) {
        loadTimeElement.textContent = now.toLocaleString('es-ES');
    }
    
    // Generar número de build aleatorio
    if (buildNumberElement) {
        const randomNum = String(Math.floor(Math.random() * 1000)).padStart(3, '0');
        buildNumberElement.textContent = `CD-2026-06-16-${randomNum}`;
    }
    
    // Verificar estado del build desde URL params
    const urlParams = new URLSearchParams(window.location.search);
    const status = urlParams.get('status');
    
    if (status === 'success') {
        // Actualizar a estado exitoso
        const buildStatus = document.getElementById('buildStatus');
        if (buildStatus) {
            buildStatus.className = 'build-status passing';
            buildStatus.innerHTML = '✅ BUILD PASSED - Todos los tests pasaron';
        }
        
        // Cambiar color de la barra de progreso
        if (progressFill) {
            progressFill.className = 'progress-fill success';
            progressFill.style.width = '100%';
        }
        
        if (progressLabel) {
            progressLabel.textContent = '100%';
        }
        
        // Cambiar el test fallido a exitoso
        const failedTest = document.getElementById('failedTest');
        if (failedTest) {
            failedTest.className = 'test-item pass';
            failedTest.innerHTML = `
                <div class="test-info">
                    <span class="status-icon">✅</span>
                    <span class="test-name">Test de división (10 ÷ 2 = 5)</span>
                </div>
                <span class="badge pass">PASS</span>
            `;
        }
        
        // Cambiar el botón
        const actionButton = document.querySelector('.button.danger');
        if (actionButton) {
            actionButton.className = 'button success';
            actionButton.textContent = '📊 Ver Actions (EXITOSO)';
            actionButton.href = 'https://github.com/Jose24Piza/CalculadoraPy/actions';
        }
    }
    
    // Simular carga inicial
    console.log('📊 CalculadoraPy CD Dashboard cargado');
    console.log(`🕐 ${now.toLocaleString('es-ES')}`);
});