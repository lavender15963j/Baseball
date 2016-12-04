$(function () {
    Highcharts.chart('chart1', {
        chart: {
            type: 'column'
        },
        title: {
            text: '得分表'
        },
        subtitle: {
            text: '得分次數 (過去150場)'
        },
        xAxis: {
            categories: [
                '1',
                '2',
                '3',
                '4',
                '5'   
            ],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: '次數 (次)'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} 次</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: '兄弟象',
            data: [20,15,30,15,20]
        },
        {
            name: '統一獅',
            data: [20,15,30,15,20]
        }
        ]
    });

    Highcharts.chart('chart2', {
        chart: {
            type: 'column'
        },
        title: {
            text: '總分合'
        },
        subtitle: {
            text: '兄弟象和統一獅得分合 (過去150場)'
        },
        xAxis: {
            categories: [
                '總分1',
                '總分2',
                '總分3',
                '總分4',
                '總分5',
                '總分6',
                '總分7',
                '總分8'  
            ],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: '次數 (次)'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} 次</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: '總分合',
            data: [15,20,10,5,20,8,12,10]
        }]
    });

    

    Highcharts.chart('chart4', {
        chart: {
            type: 'column'
        },
        title: {
            text: '贏者次數'
        },
        subtitle: {
            text: '兄弟象和統一獅 (過去150場)'
        },
        xAxis: {
            categories: [
                '象贏',
                '獅贏'
            ],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: '次數 (次)'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} 分</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: '勝者',
            data: [22,36]
        }]
    });

    Highcharts.chart('chart5', {
        chart: {
            type: 'column'
        },
        title: {
            text: '剩分差'
        },
        subtitle: {
            text: '兄弟象贏統一獅 (過去150場)'
        },
        xAxis: {
            categories: [
                '贏1分',
                '贏2分',
                '贏3分',
                '贏4分',
                '贏5分',
                '贏6分',
                '贏7分',
                '贏8分',
                '贏9分'
            ],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: '剩分差 (分)'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} 分</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: '剩分差',
            data: [4,5,1,3,7,4,5,7,9]
        }]
    });
});