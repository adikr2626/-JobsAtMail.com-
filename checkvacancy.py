#!C:\Python27\python.exe

import MySQLdb
print "Content-Type:text/html\n\n"

print """
<html>
<head>
<title>JobsAtMail</title>
<link href="adminzone/cssstyle/adminzone_style.css" rel="stylesheet" type="text/css" />
<link href="adminzone/cssstyle/adminzone_menu.css" rel="stylesheet" type="text/css" />
<link href="adminzone/cssstyle/adminzone_logo.css" rel="stylesheet" type="text/css" />

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
<div id="header"><strong><span id="sp1" style="display:none;">Welcome To JobsAtMail - Admin Zone</span></strong></div>
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
				<li style="margin-left:1250px;" class="menu_li"><a class="menu_a" href="index.py"><span class="sp1">H</span>ome</span></a></li>
			</ul>
		</div>
	</div>
<!------------------------------------------------Menu Ends---------------------------------------------->

<div id="test"></div>
<!------------------------------------------------Enquiry Starts---------------------------------------------->
<div id="enquiry" style="display:none;">
	<div id="inenquiry" style="display:none;">Enquiry</div>
</div>
<!------------------------------------------------Enquiry Ends----------------------------------------------->
<div id="container">
	<h2 style="color:#ea5b31;text-align:center;">Here are Jobs for you</h2>
	<br/>
	<table width="100%" border="1">
		<tr style="text-align:center;">
			<th style="text-align:center;">Id</th>
			<th style="text-align:center;">JobTitle</th>
			<th style="text-align:center;">Description</th>
			<th style="text-align:center;">No of post</th>
			<th style="text-align:center;">Qualification</th>
			<th style="text-align:center;">Posted Date</th>
		</tr>"""	
con=MySQLdb.connect("127.0.0.1","root","","jamdb",3306)
cmd=con.cursor()
cmd.execute("select * from vacancy order by id desc")
res=cmd.fetchall()
for row in res:
	print"<tr style='height:30px;'>"
	print"<td style='text-align:center'>",row[0],"</td>"
	print"<td style='text-align:center'>",row[1],"</td>"
	print"<td style='text-align:center'>",row[2],"</td>"
	print"<td style='text-align:center'>",row[3],"</td>"
	print"<td style='text-align:center'>",row[4],"</td>"
	print"<td style='text-align:center'>",row[5],"</td>"
	print"</tr>"
print """</table>
</div>
</div>
</body>
</html>
"""