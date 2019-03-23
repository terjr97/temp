<!DOCTYPE html>
<html>
<head>
<META HTTP-EQUIV="refresh" CONTENT="60">
<body>
<?php include('motion.php') ?>
<script>
window.onload = function () {


var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        theme: "dark2",
        title:{
                text: "People in Room"
        },
        axisY:{
                includeZero: false
        },
        data: [{
                type: "line",
                dataPoints: [
                        {x: 0, y: 1 },
                        {x: 1, y: 2 },
                        {x: 2, y: 3 },
                        {x: 3, y: 4 },
                        {x: 4, y: 3 },
                        {x: 5, y: 2 },
                        {x: 6, y: 3 },
                        {x: 7, y: 4 },
                        {x: 8, y: 5 },
                        {x: 9, y: 4 }
                ]
        }]
});
chart.render();

}
</script>
</head>
<body bgcolor="#FFFFFF">
<div id="chartContainer" style="height: 600px; width: 100%;"></div>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
</body>
</html>

