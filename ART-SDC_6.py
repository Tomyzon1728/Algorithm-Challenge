# ART
import webbrowser
s=input("enter email/website:")
if '@' in s and '.com' in s:
	print('Name: ', s.split('@')[0])
	print('Email Server: ',s.split('@')[1][:-3]) 
elif"@" in s and ".com" not in s:
	print("Please enter an Email or Website:")
else:
	webbrowser.open(s)
	
