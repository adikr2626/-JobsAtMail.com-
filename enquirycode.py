#!C:\Python27\python.exe

import cgi
import MySQLdb

print "Content-Type:text/html\n\n"

con=MySQLdb.connect("127.0.0.1","root","","jamdb",3306)
cmd=con.cursor()
data=cgi.FieldStorage()
name=data.getvalue('enqname')
address=data.getvalue('enqaddress')
contactno=data.getvalue('enqcontactno')
emailaddress=data.getvalue('enqemailaddress')
query="insert into enquiry(enqname,enqaddress,enqcontactno,enqemailaddress) values('"+name+"','"+address+"','"+contactno+"','"+emailaddress+"')"
cmd.execute(query)
con.commit()
con.close()
print "<script>alert('Your Enquiry Is Saved We Will Contact You Soon');window.location.href='index.py';</script>"