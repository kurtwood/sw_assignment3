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

			<div id="content" style="width: 50% !important; float: left !important;">
				<div id="weekchart">
					<div id="activity" class="container">
						<div class='row'>
							<div class='col-lg-12'>
								<h1>Activity <small> for all friends throughout the week </small></h1>
								<p></p>
							</div>
						</div>

					
						<div class="row">
							<div class='col-lg-6'>

								<div class='canvas'>
									<canvas id="bar" height="450" width="450"></canvas>
								</div>
							</div>
						</div>
					</div>
				</div>

				<div id="daychart" style="display: none;">
					<div id="activity" class="container">
						<div class='col-lg-12'>
							<h1>Activity <small> for all friends on (day)</small></h1>
						</div>

						<div class='canvas'>
							<canvas id="line" height="450" width="450"></canvas>
						</div>
					</div>
				</div>

			</div>

			<div id="menu-right">

				<ul>
					<li><button type="button" class="btn btn-sm btn-info">Monday</button></li>
					<li><button type="button" class="btn btn-sm btn-info">Tuesday</button></li>
					<li><button type="button" class="btn btn-sm btn-info" onclick="$('#weekchart').hide(); $('#daychart').show()">Wednesday</button></li>
					<li><button type="button" class="btn btn-sm btn-info">Thursday</button></li>
					<li><button type="button" class="btn btn-sm btn-info">Friday</button></li>
					<li><button type="button" class="btn btn-sm btn-info">Saturday</button></li>
					<li><button type="button" class="btn btn-sm btn-info">Sunday</button></li>
				</ul>

			</div>

		</div>


				<script src="js/Chart.js" type='text/javascript'></script>

				<script>

				<!-- Bar chart data -->

				var barChartData = {
					labels : ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
					datasets : [
						{
							fillColor : "rgba(151,187,205,0.5)",
							strokeColor : "rgba(151,187,205,1)",
							data : [65,59,90,81,56,55,40]
						}
					]

				}

				var myLine = new Chart(document.getElementById("bar").getContext("2d")).Bar(barChartData);

				<!-- Line chart data -->
		
				var lineChartData = {
					labels : ["00:00","06:00","12:00","18:00","24:00"],
					datasets : [
						{
							fillColor : "rgba(151,187,205,0.5)",
							strokeColor : "rgba(151,187,205,1)",
							pointColor : "rgba(151,187,205,1)",
							pointStrokeColor : "#fff",
							data : [65,59,90,81,56,55,40]
						}
					]

				}

				var myLine = new Chart(document.getElementById("line").getContext("2d")).Line(lineChartData);
		
			
				</script>

				 <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
			    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
			    <!-- Include all compiled plugins (below), or include individual files as needed -->
			    <script src="js/bootstrap.min.js"></script>

	</body>
</head>


]