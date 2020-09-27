#! /usr/bin/python3
print("content-type:text/html")
print()
import subprocess as sp
import cgi
form=cgi.FieldStorage()
cmd1=form.getvalue("x")
cmd=int(cmd1)
#osname=input("enter your os name:")
if cmd==1:
   cmd_start="sudo docker run -d -i -t --name myos     		   ubuntu:14.04"
   output=sp.getstatusoutput(cmd_start)
   status=output[0]
   out=output[1]
   if status ==0:
      print("OS launched ")
   else:
      print("some error:{}".format(out))
elif cmd==2:
   cmd_stop="sudo docker stop myos"
   output=sp.getstatusoutput(cmd_stop)
   status=output[0]
   out=output[1]
   if status ==0:
      print("OS stopped")
   else:
      print("some error:{}".format(out))
elif cmd==3:
   cmd_status="sudo docker rm myos"
   output=sp.getstatusoutput(cmd_status)
   status=output[0]
   out=output[1]
   if status ==0:
      print("os is removed")
   else:
      print("some error:{}".format(out))
