#ART
import time
import random 
import sys
import os
    
def num ( ):
    global gen_num
    global amount
    num = [str(i) for i in range (10)]
    gen_num= "".join(num)
    amount="5000"
    file = open(gen_num,'w')
    file.write(gen_num+'\n')
    file.write(amount)
    file.close()
    acc( )
    
def acc( ):
	global gen_num
	global amount 
	print("Create an Account")
	name=input("Enter full name:")
	age=input("Enter age:")
	state=input("Enter state:")
	country=input("Enter Country:")
	print("Dear "+name+"your details are:","Name:"+name,"Account number: "+gen_num,"Age: "+age,"State:"+state,"Country"+country)
	sys.exit( )
	print("Your account balance is: "+"N"+amount)
gen_num=" "	
a=0
while a<3:
	a+=1
	s=time.time()
	p=input("enter pin:")
	n=input("account number:")
	e=time.time()
	file = open(p,'w')
	file.write(p+'\n')
	file.write(n)
	file.close()
	if e-s >15:
		print("Time exceeded, try again!")
		continue
	file_list = os.listdir()
	if p in  file_list:
	       file1 = open(p, 'r')
	       verify = file1.read().splitlines()
	       if n in verify:
	       	num()
    

	
		
	
