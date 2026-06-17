document.addEventListener('DOMContentLoaded', function() {
    console.log('📊 CalculadoraPy CD Dashboard cargado');
    
    const elements = {
        buildStatus: document.getElementById('buildStatus'),
        alertMessage: document.getElementById('alertMessage'),
        buildNumber: document.getElementById('buildNumber'),
        timestamp: document.getElementById('timestamp'),
        buildStatusText: document.getElementById('buildStatusText'),
        progressFill: document.getElementById('progressFill'),
        progressLabel: document.getElementById('progressLabel'),
        loadTime: document.getElementById('loadTime'),
        testSuma: document.getElementById('testSuma'),
        testResta: document.getElementById('testResta'),
        testMultiplicacion: document.getElementById('testMultiplicacion'),
        testDivision: document.getElementById('testDivision'),
        testDivisionCero: document.getElementById('testDivisionCero'),
        testIntegracion: document.getElementById('testIntegracion')
    };
    
    // Actualizar timestamp
    const now = new Date();
    if (elements.timestamp) {
        elements.timestamp.textContent = now.toLocaleString('es-ES');
    }
    if (elements.loadTime) {
        elements.loadTime.textContent = now.toLocaleString('es-ES');
    }
    
    // SIMULACIÓN DE TESTS - Todos pasan
    function simulateTests() {
        const testResults = {
            suma: true,
            resta: true,
            multiplicacion: true,
            division: true,
            divisionCero: true,
            integracion: true
        };
        
        // Para probar fallo, descomentar:
        // testResults.division = false;
        
        updateTestResults(testResults);
    }
    
    function updateTestResults(results) {
        const allPassed = Object.values(results).every(v => v === true);
        const progress = (Object.values(results).filter(v => v === true).length / Object.values(results).length) * 100;
        
        if (elements.progressFill) {
            elements.progressFill.style.width = progress + '%';
        }
        if (elements.progressLabel) {
            elements.progressLabel.textContent = Math.round(progress) + '%';
        }
        
        const testMap = {
            suma: elements.testSuma,
            resta: elements.testResta,
            multiplicacion: elements.testMultiplicacion,
            division: elements.testDivision,
            divisionCero: elements.testDivisionCero,
            integracion: elements.testIntegracion
        };
        
        Object.keys(testMap).forEach(key => {
            const element = testMap[key];
            if (element) {
                const passed = results[key];
                element.className = `test-item ${passed ? 'pass' : 'fail'}`;
                element.querySelector('.status-icon').textContent = passed ? '✅' : '❌';
                element.querySelector('.badge').textContent = passed ? 'PASS' : 'FAIL';
                element.querySelector('.badge').className = `badge ${passed ? 'pass' : 'fail'}`;
            }
        });
        
        if (elements.buildStatus) {
            if (allPassed) {
                elements.buildStatus.className = 'build-status passing';
                elements.buildStatus.textContent = '✅ BUILD PASSED - Todos los tests pasaron';
            } else {
                elements.buildStatus.className = 'build-status failing';
                elements.buildStatus.textContent = `❌ BUILD FAILED - ${Object.values(results).filter(v => v === false).length} tests fallaron`;
            }
        }
        
        if (elements.alertMessage) {
            if (allPassed) {
                elements.alertMessage.className = 'alert success';
                elements.alertMessage.innerHTML = '✅ Todos los tests han pasado correctamente 🎉';
            } else {
                elements.alertMessage.className = 'alert error';
                elements.alertMessage.innerHTML = '❌ Algunos tests han fallado. Revisa GitHub Actions.';
            }
        }
        
        if (elements.buildStatusText) {
            if (allPassed) {
                elements.buildStatusText.innerHTML = '✅ EXITOSO';
                elements.buildStatusText.style.color = '#28a745';
            } else {
                elements.buildStatusText.innerHTML = '❌ FALLIDO';
                elements.buildStatusText.style.color = '#dc3545';
            }
        }
        
        if (elements.buildNumber) {
            const randomNum = String(Math.floor(Math.random() * 1000)).padStart(3, '0');
            elements.buildNumber.textContent = `CD-${now.toISOString().split('T')[0]}-${randomNum}`;
        }
    }
    
    simulateTests();
});