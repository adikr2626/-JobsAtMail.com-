#!C:\Python27\python.exe
import MySQLdb

print "Content-Type:text/html\n\n"

print """
<html>
<head>
<title>JobsAtMail</title>
<link href="cssstyle/style.css" rel="stylesheet" type="text/css" />
<link href="cssstyle/menu.css" rel="stylesheet" type="text/css" />
<link href="cssstyle/logo.css" rel="stylesheet" type="text/css" />
<link href="cssstyle/enquiry.css" rel="stylesheet" type="text/css" />
<link href="cssstyle/icons.css" rel="stylesheet" type="text/css" />

 <meta charset="utf-8">
 <meta http-equiv="X-UA-Compatible" content="IE=edge">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css" />
 <link href="css/bootstrap-theme.min.css" rel="stylesheet" type="text/css" />

  <script src="js/jquery.js" rel="javascript" type="text/javascript"></script>
 <script src="js/bootstrap.min.js" rel="javascript" type="text/javascript"></script>

 <script src="jquery-3.3.1.min.js"></script>
 <script>
$(document).ready(function(){
//header
$('#header').show(2000);
$('#sp1').slideDown(7000);
//enquiry
$('#inenquiry').click(function(){
	$('#enq').fadeToggle(1000);
})
//enquiry Submit
$('#enqsubmit').click(function(){
	$('#enq').fadeOut(1000);
})

})
</script>
 </head>
<body>
<!------------------------------------------------Header Starts---------------------------------------------->
<div id="header"><strong><span id="sp1" style="display:none;">Welcome To JobsAtMail</span></strong></div>
<!------------------------------------------------Header Ends------------------------------------------------>
<div id="wrapper">
<!------------------------------------------------Menu Starts---------------------------------------------->
	<div id="menu">
		<div class="lmenu">
			<div class="logo">
				JobsAtMail
			</div>
		</div>
		<div class="rmenu">
			<ul class="menu_ul">
				<li class="menu_li"><a class="menu_a" href="index.py"><span class="home"><span class="sp1">H</span>ome</span></a></li>
				<li class="menu_li"><a id="a" class="menu_a" href="#about"><span class="sp1">A</span>bout Us</a></li>
				<li class="menu_li"><a class="menu_a" href="registration.py"><span class="sp1">R</span>egistration</a></li>
				<li class="menu_li"><a class="menu_a" href="login.py"><span class="sp1">L</span>ogin</a></li>
				<li class="menu_li"><a class="menu_a" href="enquiryform.py"><span class="sp1">E</span>nquiry</a></li>
				<li class="menu_li"><a class="menu_a" href="checkvacancy.py"><span class="sp1">V</span>acancy</a></li>
			</ul>
		</div>
	</div>
<!------------------------------------------------Menu Ends---------------------------------------------->

<!------------------------------------------------Slider Starts---------------------------------------------->
	<div id="slider">
	<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
  <!--Indicators-->
  <ol class="carousel-indicators">
    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
    <li data-target="#carousel-example-generic" data-slide-to="1"></li>
    <li data-target="#carousel-example-generic" data-slide-to="2"></li>
  </ol>

  <!--Wrapper for slides-->
  <div class="carousel-inner" role="listbox">
    <div class="item active">
      <img src="images/1.jpg" alt="..." style="width:100%;height:450px;">
      <div class="carousel-caption" style="font-size:30px;">
        1
      </div>
    </div>
    <div class="item">
      <img src="images/2.jpg" alt="..." style="width:100%;height:450px;">
      <div class="carousel-caption" style="font-size:30px;">
        2
      </div>
    </div>
    <div class="item">
      <img src="images/3.jpg" alt="..." style="width:100%;height:450px;">
      <div class="carousel-caption" style="font-size:30px;">
        3
      </div>
    </div>
  </div>

  <!--Controls-->
  <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
</div>
<!------------------------------------------------Slider Ends---------------------------------------------->
<div id="test"><marquee direction="up" behavior="alternate" scrollspeed="" height="100%" onmouseover="this.stop()" onmouseout="this.start()" scrollamount="2">"""
con=MySQLdb.connect("127.0.0.1","root","","jamdb",3306)
cmd=con.cursor()
query="select * from notification order by id desc"
cmd.execute(query)
res=cmd.fetchall()
for row in res:
	print "<p><b>Notification:</b></p>"
	print "<p>",row[1],"</p>"
	print "<p><b>Date:</b></p>"
	print "<p>",row[2],"</p>"
	print "<hr/>"
print"""</marquee></div>
<div id="about" >
	<h2 class="abouthead">About Us</h2><br/>
	<h3 class="matter1">JobsAtMail.com welcomes you, we are here to lead your success. You can register here by filling registration form and then you can search jobs according to your qualificatipons, experiences and skilss.</h3>
	<h3 class="matter1">Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.</h3>
	<h3 class="matter1">Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum dolor sit amet.Lorem ipsum</h3>
</div>

<div id="footer">
	<div id="lfooter">
		<a href="#" target="blank"><img src="images/fb.png" style="height:25px;width:25px;margin-top:25px;margin-left:50px;"></a>
		<a href="#" target="blank"><img src="images/twitter.png" style="height:25px;width:25px;margin-top:25px;margin-left:20px;"></a>
		<a href="#" target="blank"><img src="images/wifi.jpg" style="height:25px;width:25px;margin-top:25px;margin-left:20px;"></a>
	</div>
	<div id="rfooter">
		<font class="rf"><span id="sprf">Developed By:</span> Aditya Kr Kashyap</font>
	</div>
</div>

</div><!--closing div of wrapper-->

<!------------------------------------------------Enquiry Starts---------------------------------------------->



<!------------------------------------------------Enquiry Ends----------------------------------------------->
</body>
</html>
"""