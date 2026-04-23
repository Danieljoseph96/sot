(function () {
    var chartCanvas = document.getElementById('meetingChart');
    if (!chartCanvas || typeof Chart === 'undefined') {
        return;
    }

    var labelsElement = document.getElementById('chart-labels');
    var valuesElement = document.getElementById('chart-values');

    if (!labelsElement || !valuesElement) {
        return;
    }

    var labels = JSON.parse(labelsElement.textContent);
    var values = JSON.parse(valuesElement.textContent);

    new Chart(chartCanvas, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Meetings',
                data: values,
                borderColor: '#0d6efd',
                backgroundColor: 'rgba(13, 110, 253, 0.15)',
                tension: 0.35,
                fill: true
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
})();
