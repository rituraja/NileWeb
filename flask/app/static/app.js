
$(function() {
  $.getJSON('/showChart1', function(data) {
    data.chart = {"renderTo": "chart1", "type": 'bar', "height": 500};
    $("#chart1").highcharts(data);
  });
});
