#!C:\Python27\python.exe

import cgi
import MySQLdb

print "Content-Type:text/html\n\n"

data=cgi.FieldStorage()
name=data.getvalue('name')
gender=data.getvalue('gender')
address1=data.getvalue('address1')
address2=data.getvalue('address2')
zipcode=int(data.getvalue('zipcode'))
qualification=data.getvalue('qualification')
experience=int(data.getvalue('experience'))
lastcompany=data.getvalue('lastcompany')
expertisearea=data.getvalue('expertisearea')
keyskills=data.getvalue('keyskills')
contactno=data.getvalue('contactno')
emailaddress=data.getvalue('emailaddress')
adharno=data.getvalue('adharno')
panno=data.getvalue('panno')
password=data.getvalue('password')
con=MySQLdb.connect("127.0.0.1","root","","jamdb",3306)

cmd=con.cursor()
query1="insert into jobseekerinfo values('"+name+"','"+gender+"','"+address1+"','"+address2+"','"+str(zipcode)+"','"+qualification+"','"+str(experience)+"','"+lastcompany+"','"+expertisearea+"','"+keyskills+"','"+contactno+"','"+emailaddress+"','"+adharno+"','"+panno+"','"+password+"','false')"
query2="insert into login values('"+contactno+"','"+password+"','user')"
cmd.execute(query1)
cmd.execute(query2)
con.commit()
con.close()
print "<script>alert('registration successfull');window.location.href='index.py'</script>"