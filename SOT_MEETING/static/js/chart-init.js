(function () {
    if (typeof Chart === 'undefined') {
        return;
    }

    function readJsonScript(id) {
        var element = document.getElementById(id);
        if (!element) {
            return null;
        }
        return JSON.parse(element.textContent);
    }

    function createChart(config) {
        var canvas = document.getElementById(config.canvasId);
        var labels = readJsonScript(config.labelsId);
        var values = readJsonScript(config.valuesId);

        if (!canvas || !labels || !values || !labels.length || !values.length) {
            return;
        }

        new Chart(canvas, {
            type: config.type,
            data: {
                labels: labels,
                datasets: [{
                    label: config.label,
                    data: values,
                    backgroundColor: config.backgroundColor,
                    borderColor: config.borderColor,
                    borderWidth: 2,
                    tension: 0.3,
                    fill: config.fill || false
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    createChart({
        canvasId: 'paymentStatusChart',
        labelsId: 'payment-chart-labels',
        valuesId: 'payment-chart-values',
        type: 'doughnut',
        label: 'Payment methods',
        backgroundColor: ['#198754', '#0d6efd', '#ffc107', '#dc3545', '#6f42c1'],
        borderColor: '#ffffff'
    });

    createChart({
        canvasId: 'registrationLocalityChart',
        labelsId: 'registration-chart-labels',
        valuesId: 'registration-chart-values',
        type: 'bar',
        label: 'Registered people',
        backgroundColor: 'rgba(13, 110, 253, 0.35)',
        borderColor: '#0d6efd'
    });

    createChart({
        canvasId: 'userregLocalityChart',
        labelsId: 'locality-chart-labels',
        valuesId: 'locality-chart-values',
        type: 'line',
        label: 'UserReg entries',
        backgroundColor: 'rgba(25, 135, 84, 0.15)',
        borderColor: '#198754',
        fill: true
    });
})();
