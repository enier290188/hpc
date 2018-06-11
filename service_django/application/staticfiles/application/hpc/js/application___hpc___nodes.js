var hpc_nodes_datatable = function(){
    var optionsDataTable = {
        dom: "frti",
        responsive: true
    };
    $("#datatable-nodes").DataTable(optionsDataTable);
};

var hpc_nodes_chart = function(){
    var ctx = document.getElementById("myLineChart").getContext("2d");
    var myLineChart, data = [,,,,,,,,,,,,parseInt(cpuload)];

    var ctxDoughnut = document.getElementById("myDoughnutChart").getContext("2d");
    var myDoughnutChart, percent;

    var ctxDoughnut2 = document.getElementById("myDoughnutChart2").getContext("2d");
    var myDoughnutChart2, percent2;

    Chart.defaults.global.legend.labels.boxWidth = 12;
    myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["60",,"50",,"40",,"30",,"20",,"10",,"0"], //labels: ["60", ,"50", ,"40", ,"30", ,"20", ,"10", ,"0"],
            datasets: [{
                label: gettext('HPC___CONTENT___NODES___CHART_LINE'),
                fill: true,
                lineTension: 0,
                pointRadius: 0,
                borderWidth: 1,
                pointHitRadius: 0,
                backgroundColor: "rgba(255,10,10,0.6)",
                borderColor: "rgba(255,10,10,1)",
                borderJoinStyle: 'miter',
                data: data
            }]
        },
        options: {
            responsive: true,
            scales: {
                yAxes: [{
                    ticks: {
                        suggestedMax:100, suggestedMin:0
                    }
                }]
            }
        }
    });

    percent = Math.round(100*parseInt(allocmem)/parseInt(freemem));
    myDoughnutChart = new Chart(ctxDoughnut, {
        type: 'doughnut',
        data: {
            labels: [
               gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_1_Assigned_mem') + percent + '%',
               gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_1_Free_mem') +(100 - percent) + '%'
            ],
            datasets: [
                {
                    data: [parseInt(allocmem), parseInt(freemem) - parseInt(allocmem)],
                    backgroundColor: [
                        "#FF6384", "#36A2EB"
                    ],
                    hoverBackgroundColor: [
                        "#FF6384", "#36A2EB"
                    ]
                }
            ]
        },
        options: {
            responsive: true
        }
    });

    percent2 = Math.round(100*parseInt(cpualloc)/parseInt(cputot));
    myDoughnutChart2 = new Chart(ctxDoughnut2, {
        type: 'doughnut',
        data: {
            labels: [
                gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_2_Assigned_CPUs') + percent2 + '%',
                gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_2_Free_CPUs') +(100 - percent2) + '%'
            ],
            datasets: [
                {
                    data: [parseInt(cpualloc), parseInt(cputot) - parseInt(cpualloc)],
                    backgroundColor: [
                        "#FF6384", "#FF9933"
                    ],
                    hoverBackgroundColor: [
                        "#FF6384", "#FF9933"
                    ]
                }
            ]
        },
        options: {
            responsive: true
        }
    });

    var myTimer = setInterval(function () {
        if ($("#myLineChart").length) {
            $.ajax({
                url: url_chartnodes,
                type: 'get',
                cache: false,
                dataType: 'json',
                success: function (response) {
                    //LineChart
                    console.log(response);
                    var number = response.statistics.cpuload;
                    for (var i = 0; i < data.length; i++)
                        if (i === data.length - 1)
                            data[i] = number;
                        else
                            data[i] = data[i + 1];
                    myLineChart.data = data;
                    myLineChart.update(0);

                    //DoughnutChart
                    var freemem = response.statistics.freemem;
                    var allocmem = response.statistics.allocmem;
                    percent = Math.round(100 * allocmem / freemem);
                    myDoughnutChart.data.labels[0] = gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_1_Assigned_mem') + percent + '%';
                    myDoughnutChart.data.labels[1] = gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_1_Free_mem') + (100 - percent) + '%';
                    myDoughnutChart.data.datasets[0].data[0] = allocmem;
                    myDoughnutChart.data.datasets[0].data[1] = freemem - allocmem;
                    myDoughnutChart.update(0);

                    //DoughnutChart2
                    var cpualloc = response.statistics.cpualloc;
                    var cputot = response.statistics.cputot;
                    percent2 = Math.round(100 * cpualloc / cputot);
                    myDoughnutChart2.data.labels[0] = gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_2_Assigned_CPUs') + percent2 + '%';
                    myDoughnutChart2.data.labels[1] = gettext('HPC___CONTENT___NODES___CHART_DOUGHNUT_2_Free_CPUs') + (100 - percent2) + '%';
                    myDoughnutChart2.data.datasets[0].data[0] = cpualloc;
                    myDoughnutChart2.data.datasets[0].data[1] = cputot - cpualloc;
                    myDoughnutChart2.update(0);
                },
                error: function (response) {
                }
            });
        }
        else {
            clearInterval(myTimer);
        }
    }, 5000);
};

hpc_nodes_datatable();
hpc_nodes_chart();
