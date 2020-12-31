#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"

print"""
<html>
<head>
<title>JobsAtMail_Login</title>
<link href="cssstyle/loginstyle.css" rel="stylesheet" type="text/css"/>

<script src="jquery-3.3.1.min.js"></script>
<script>
$(document).ready(function(){
//header
$('#header').fadeIn(2000);
$('#sp1').slideDown(2000);
})
</script>
</head>
<body>
<form action="logcode.py" method="post">
<!------------------------------------------------Header Starts---------------------------------------------->
<div id="header"><strong><span id="sp1" style="display:none;">Welcome To JobsAtMail - Login Form</span></strong></div>
<!------------------------------------------------Header Ends------------------------------------------------>
<div id="wrapper">
	<br/><br/>
	<font id="fnt1" class="font">UserId :</font>
	<br/><br/>
	<input type="text" name="userid" />
	<br/><br/><br/>
	<font class="font">Password :</font>
	<br/><br/>
	<input type="password" name="password" />
	<br/><br/><br/><br/>
	<input class="submit" type="submit" value="Login">
</div>
</form>
</body>
</html>
"""