#!C:\Python27\python.exe

print "Content-Type:text/html\n\n"

print """
<html>
<head>
<title>Registration</title>
<link href="cssstyle/registrationstyle.css" rel="stylesheet" type="text/css" />

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
})
</script>
</head>
<body>
<!------------------------------------------------Header Starts---------------------------------------------->
<div id="header"><strong><span id="sp1" style="display:none;">Welcome To JobAtMail - Registration Form</span></strong></div>
<!------------------------------------------------Header Ends------------------------------------------------>

<form action="regcode.py" method="post">
	<div id="wrapper">
		<br/>
		<font class="font">Enter Name :</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<input id="inp1" onblur="formValidate()" type="text" name="name" maxlength="50" /><span id="sp1"></span>
		<br/><br/>
		<font class="font">Select Gender :</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<input type="radio" name="gender" value="male" style="width:20px;" checked /><span class="gender_text">Male</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<input type="radio" name="gender" value="female" style="width:20px;" /><span class="gender_text">Female</span>
		<br/><br/>
		<font class="font">Enter Address1 :</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<textarea id="inp2" class="addresses" cols="92" rows="4" name="address1" maxlength="100"></textarea>
		<br/><br/>
		<font class="font">Enter Address2 :</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<textarea id="inp3" class="addresses" cols="92" rows="4" name="address2" maxlength="100"></textarea>
		<br/><br/>
		<font class="font">Enter Zipcode :</font>&nbsp;&nbsp;	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<input id="inp4" type="text" name="zipcode" maxlength="11" />
		<br/><br/>
		<font class="font">Qualification :</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<select class="select_quali" name="qualification">
			<option>---- Select Qualification ----</option>
			<option>B.Tech.</option>
			<option>M.Tech.</option>
			<option>B.C.A</option>
			<option>B.B.A</option>
		</select>
		<br/><br/>
		<font class="font">Experience :</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<input id="inp5" type="number" name="experience" />
		<br/><br/>
		<font class="font">Last Company :</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<input id="inp6" type="text" name="lastcompany" maxlength="50" />
		<br/><br/>
		<font class="font">Expertise Area :</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<input id="inp7" type="text" name="expertisearea" maxlength="50" />
		<br/><br/>
		<font class="font">Key Skills :</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<textarea id="inp8" class="addresses" cols="95" rows="4" name="keyskills" maxlength="500"></textarea>
		<br/><br/>
		<font class="font">Contact No :</font>&nbsp;&nbsp;&nbsp;&nbsp;	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<input id="inp9" type="text" name="contactno" maxlength="15" />
		<br/><br/>
		<font class="font">Email Address :</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<input id="inp10" type="email" name="emailaddress" maxlength="50" />
		<br/><br/>
		<font class="font">Adhar Number :</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<input id="inp11" type="text" name="adharno" maxlength="20" />
		<br/><br/>
		<font class="font">Pan Number :</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<input id="inp12" type="text" name="panno" maxlength="20" />
		<br/><br/>
		<font class="font"> Password :</font>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<input id="inp13" type="password" name="password" maxlength="20" />
		<br/><br/><br/>
		<input class="submitbtn" type="submit" value="Register" />
	</div>
</form>
</body>
</html>
"""