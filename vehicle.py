#!/usr/bin/python3
import cgi
import os
import subprocess as sp
print("content-type: text/html")
print()
f=cgi.FieldStorage()
cmd = f.getvalue("x")

if cmd == "MH 20 EE 7598":
	print('''<pre>
	Car Number: HR26DQ5551
	Car Model: KIA
	Registration Name: Srushti 
	Registration Date: 10/1/2013
	Fuel Type: CNG
	Location: Haryana, India
	Vehicle Class: SUV
	Insurance Upto: 10/12/2022
	</pre>''')
elif cmd == "GJ 5 CL 2213":
	print('''<pre>
	Car Number: GJ 5 CL 2213
	Car Model: BMW
	Registration Name: Vrukshali
	Registration Date: 10/7/2016
	Fuel Type: CNG
	Location: Maharashtra , India
	Vehicle Class: SUV
	Insurance Upto: 19/12/2026
	</pre>''')

elif cmd == "HR26DQ5551":
	print('''<pre>
	Car Number: HR26DQ5551
	Car Model: HONDA CITY
	Registration Name: Anuja
	Registration Date: 10/1/2015
	Fuel Type: CNG
	Location: Gujarat, India
	Vehicle Class: SUV
	Insurance Upto: 19/12/2025
	</pre>''')
else:
	 "no car found"