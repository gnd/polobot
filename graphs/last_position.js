// legend callback - see https://www.chartjs.org/docs/latest/configuration/legend.html
function legendCallbackPolobot(e, legendItem) {
    var index = legendItem.datasetIndex;
    var ci = this.chart;
    var meta = ci.getDatasetMeta(index);
    meta.hidden = meta.hidden === null ? !ci.data.datasets[index].hidden : null;

    // Update the chart
    ci.update();
}

// Define graphs
var last_position_daily_graph = document.getElementById("last_position_daily_canvas").getContext('2d');
var last_position_weekly_graph = document.getElementById("last_position_weekly_canvas").getContext('2d');
var last_position_monthly_graph = document.getElementById("last_position_monthly_canvas").getContext('2d');

// Create datasets
dataset_daily = [];
dataset_daily.push( {
    label: 'BTC_DCR',
    data: last_position['daily']['BTC_DCR']['data'],
    spanGaps: true,
    borderWidth: 1,
    borderColor: '#' + pal_8[0],
    pointStyle: 'cross',
    pointBorderColor:  '#' + pal_8[0],
    tension: 0,
    fill: false
} );
dataset_daily.push( {
    label: 'BTC_DCR rolling avg hourly',
    data: last_position['daily']['BTC_DCR']['avg_hourly'],
    spanGaps: true,
    borderWidth: 1,
    borderColor: '#' + pal_8[1],
    pointStyle: 'cross',
    pointBorderColor:  '#' + pal_8[1],
    tension: 0,
    fill: false
} );
dataset_weekly = [];
dataset_weekly.push( {
    label: 'BTC_DCR',
    data: last_position['weekly']['BTC_DCR']['data'],
    spanGaps: true,
    borderWidth: 1,
    borderColor: '#' + pal_8[0],
    pointStyle: 'cross',
    pointBorderColor:  '#' + pal_8[0],
    tension: 0,
    fill: false
} );
dataset_weekly.push( {
    label: 'BTC_DCR rolling avg daily',
    data: last_position['weekly']['BTC_DCR']['avg_daily'],
    spanGaps: true,
    borderWidth: 1,
    borderColor: '#' + pal_8[1],
    pointStyle: 'cross',
    pointBorderColor:  '#' + pal_8[1],
    tension: 0,
    fill: false
} );
dataset_monthly = [];
dataset_monthly.push( {
    label: 'BTC_DCR',
    data: last_position['monthly']['BTC_DCR']['data'],
    spanGaps: true,
    borderWidth: 1,
    borderColor: '#' + pal_8[0],
    pointStyle: 'cross',
    pointBorderColor:  '#' + pal_8[0],
    tension: 0,
    fill: false
} );
dataset_monthly.push( {
    label: 'BTC_DCR rolling avg weekly',
    data: last_position['monthly']['BTC_DCR']['avg_weekly'],
    spanGaps: true,
    borderWidth: 1,
    borderColor: '#' + pal_8[1],
    pointStyle: 'cross',
    pointBorderColor:  '#' + pal_8[1],
    tension: 0,
    fill: false
} );

// Last position daily chart
window.last_position_daily_chart = new Chart(last_position_daily_graph, {
    type: 'line',
    data: {
        labels: last_position['daily']['BTC_DCR']['labels'],
        datasets: dataset_daily,
    },
    options: {
        aspectRatio: aspect_ratio,
        title: {
            display: true,
            fontSize: fontsize,
            text: ["Price in the last 24 Hours correlated with last_position"]
        },
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'minute'
                }
            }],
            yAxes: [{
                ticks: {
                    min: 0,
                    suggestedMax: 1,
                }
            }]
        },
        legend: {
            display: true,
            onClick: legendCallbackPolobot,
            labels: {
                fontSize: fontsize,
            }
        },
    }
});

// Last position weekly chart
window.last_position_weekly_chart = new Chart(last_position_weekly_graph, {
    type: 'line',
    data: {
        labels: last_position['weekly']['BTC_DCR']['labels'],
        datasets: dataset_weekly,
    },
    options: {
        aspectRatio: aspect_ratio,
        title: {
            display: true,
            fontSize: fontsize,
            text: ["Price in the last 7 days correlated with last_position"]
        },
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'minute'
                }
            }],
            yAxes: [{
                ticks: {
                    min: 0,
                    suggestedMax: 1,
                }
            }]
        },
        legend: {
            display: true,
            onClick: legendCallbackPolobot,
            labels: {
                fontSize: fontsize,
            }
        },
    }
});

// Last position monthly chart
window.last_position_monthly_chart = new Chart(last_position_monthly_graph, {
    type: 'line',
    data: {
        labels: last_position['monthly']['BTC_DCR']['labels'],
        datasets: dataset_monthly,
    },
    options: {
        aspectRatio: aspect_ratio,
        title: {
            display: true,
            fontSize: fontsize,
            text: ["Price in the last 30 days correlated with last_position"]
        },
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'minute'
                }
            }],
            yAxes: [{
                ticks: {
                    min: 0,
                    suggestedMax: 1,
                }
            }]
        },
        legend: {
            display: true,
            onClick: legendCallbackPolobot,
            labels: {
                fontSize: fontsize,
            }
        },
    }
});
