
$(function() {
  $.getJSON('/showChart1', function(data) {
    data.chart = {renderTo: "chart1", type: 'bar', height: 500};
    data.plotOptions = {series: {colorByPoint: true}};
    $("#chart1").highcharts(data);
  });

  $.getJSON('/api/getSalesPerCategory_daily/2014-12-28', function(data) {
    data.chart = {renderTo: "chart2", type: 'bar', height: 500};
    data.plotOptions = {series: {colorByPoint: true}};
    $("#chart2").highcharts(data);
  });

$.getJSON('/api/getSalesPerCategory_monthly/2014_12', function(data) {
    data.chart = {renderTo: "chart3", type: 'bar', height: 500};
    data.plotOptions = {series: {colorByPoint: true}};
    $("#chart3").highcharts(data);
  });

});

