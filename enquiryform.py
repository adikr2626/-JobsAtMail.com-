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
<link href="cssstyle/enqform.css" rel="stylesheet" type="text/css" />

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
$('#header').fadeIn(2000);
$('#sp1').slideDown(2000);
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
				<li class="menu_li"><a class="menu_a" href="#"><span class="sp1">A</span>bout Us</a></li>
				<li class="menu_li"><a class="menu_a" href="registration.py"><span class="sp1">R</span>egistration</a></li>
				<li class="menu_li"><a class="menu_a" href="login.py"><span class="sp1">L</span>ogin</a></li>
				<li class="menu_li"><a class="menu_a" href="#"><span class="sp1">E</span>nquiry</a></li>
			</ul>
		</div>
	</div>
<!------------------------------------------------Menu Ends---------------------------------------------->
<form action="enquirycode.py" method="post">
<div id="enqform">

	<form action="enquirycode.py" method="post"><br/>
	<font class="enqfont">Name :</font>
	<br/>
	<input class="enqinput" type="text" name="enqname" maxlength="50" required />
	<br/><br/><br/>
	<font class="enqfont">Address :</font>
	<br/>
	<textarea class="enqaddr" name="enqaddress" cols="75" rows="4" maxlength="100" required ></textarea>
	<br/><br/><br/>
	<font class="enqfont">Contact No :</font>
	<br/>
	<input class="enqinput" type="text" name="enqcontactno" maxlength="15" required />
	<br/><br/><br/>
	<font class="enqfont">Email Id :</font>
	<br/>
	<input class="enqinput" type="email" name="enqemailaddress" maxlength="50" required />
	<br/><br/><br/><br/>
	<input class="enqsubmit" type="submit" value="Submit" />
</div>
</form>
<div id="footer">
	<div id="lfooter">
		<i class="glyphicon glyphicon-envelope"></i>
		<i class="glyphicon glyphicon-home"></li>
	</div>
	<div id="rfooter"></div>
</div>

</div><!--closing div of wrapper-->

<!------------------------------------------------Enquiry Starts---------------------------------------------->



<!------------------------------------------------Enquiry Ends----------------------------------------------->
</body>
</html>
"""