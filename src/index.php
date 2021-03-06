<!DOCTYPE html>
<html>
	<head>
		
		<title>SW Facebook activity checker</title>
		
		<link rel="stylesheet" type="text/css" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
		<link rel="stylesheet" type="text/css" href="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap-theme.min.css">
		<link rel="stylesheet" type="text/css" href="style.css">

		<script type="text/javascript" src="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
		

	</head>

	<body>
		<div id="wrapper">

			<?php include 'menu.php'; ?>

			<div id="content">

				<div id="likes" class="container">
					<div class='row'>
						<div class='col-lg-12'>
							<h1>SW Facebook activity checker</h1>
							<p></p>
						</div>
					</div>

					<div class="btn-group">
		  				<a href="#likes" anchorLink><button class="btn">Likes</button></a>
		  				<a href="#statuses" anchorLink><button class="btn">Statuses</button></a>
		  				<a href="#activity" anchorLink><button class="btn">Activity</button></a>
					</div>

					<div class='row'>
						<div class='col-lg-6'>
							<h3>Number of likes  <small> for all people active in a given category</small></h3>
							<p></p>
							
							<div class='canvas'>
								<canvas id="doughnut" height="450" width="450"></canvas>
							</div>
						</div>
					</div>
				</div>	

				<div id="statuses" class="container">
					<div class='row'>
						<div class='col-lg-12'>
							<h1>SW Facebook activity checker</h1>
							<p></p>
						</div>
					</div>

					<div class="btn-group">
		  				<a href="#likes" anchorLink><button class="btn">Likes</button></a>
		  				<a href="#statuses" anchorLink><button class="btn">Statuses</button></a>
		  				<a href="#activity" anchorLink><button class="btn">Activity</button></a>
					</div>
				
					<div class="row">
						<div class='col-lg-6'>
							<h3>Number of statuses <small> for all people active in a given category </small> </h3>
							<p></p>
							
							<div class='canvas'>
								<canvas id="pie" height="450" width="450"></canvas>
							</div>
						</div>	
					</div>
				</div>	

				<div id="activity" class="container">
					<div class='row'>
						<div class='col-lg-12'>
							<h1>SW Facebook activity checker</h1>
							<p></p>
						</div>
					</div>

					<div class="btn-group">
		  				<a href="#likes" anchorLink><button class="btn">Likes</button></a>
		  				<a href="#statuses" anchorLink><button class="btn">Statuses</button></a>
		  				<a href="#activity" anchorLink><button class="btn">Activity</button></a>
					</div>

					<div class="row">
						<div class='col-lg-6'>
							<h3>Activity <small> for all friends throughout the week </small> </h3>
							<p></p>

							<div class='canvas'>
								<canvas id="bar" height="450" width="450"></canvas>
							</div>
						</div>
					</div>
				</div>

			</div>

		</div>

				<script src="js/Chart.js" type='text/javascript'></script>

				<script>

				<!-- Doughnut chart data -->

				var doughnutData = [
						{
							value: 30,
							color:"#F7464A"
						},
						{
							value : 50,
							color : "#46BFBD"
						},
						{
							value : 100,
							color : "#FDB45C"
						},
						{
							value : 40,
							color : "#949FB1"
						},
						{
							value : 120,
							color : "#4D5360"
						}

					];

				var myDoughnut = new Chart(document.getElementById("doughnut").getContext("2d")).Doughnut(doughnutData);


				<!-- Line chart data -->
		/*
				var lineChartData = {
					labels : ["00:00","06:00","12:00","18:00","24:00"],
					datasets : [
						{
							fillColor : "rgba(220,220,220,0.5)",
							strokeColor : "rgba(220,220,220,1)",
							pointColor : "rgba(220,220,220,1)",
							pointStrokeColor : "#fff",
							data : [65,59,90,81,56,55,40]
						},
						{
							fillColor : "rgba(151,187,205,0.5)",
							strokeColor : "rgba(151,187,205,1)",
							pointColor : "rgba(151,187,205,1)",
							pointStrokeColor : "#fff",
							data : [28,48,40,19,96,27,100]
						}
					]

				}

				var myLine = new Chart(document.getElementById("line").getContext("2d")).Line(lineChartData);
		*/
				<!-- Bar chart data -->

				var barChartData = {
					labels : ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
					datasets : [
						{
							fillColor : "rgba(220,220,220,0.5)",
							strokeColor : "rgba(220,220,220,1)",
							data : [65,59,90,81,56,55,40]
						},
						{
							fillColor : "rgba(151,187,205,0.5)",
							strokeColor : "rgba(151,187,205,1)",
							data : [28,48,40,19,96,27,100]
						}
					]

				}

				var myLine = new Chart(document.getElementById("bar").getContext("2d")).Bar(barChartData);


				<!-- Pie chart data -->
					var pieData = [
						{
							value: 30,
							color:"#F38630"
						},
						{
							value : 50,
							color : "#E0E4CC"
						},
						{
							value : 100,
							color : "#69D2E7"
						}

					];

				var myPie = new Chart(document.getElementById("pie").getContext("2d")).Pie(pieData);
				console.log("Hei");
				</script>

				 <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>

	</body>
</head>


