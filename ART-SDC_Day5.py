# ART
import os
import sys
def mp3( ):
	print("Mp3 files\t\t : \t\tsize")
	all_files = os.listdir("/storage/emulated/0/Download")
	mp3_files = [f for f in all_files  if f.endswith(".mp3")]
	times=len(mp3_files)
	print("Number of Mp3 files:",times)
	for i in mp3_files:
		st = os.path.getsize("/storage/emulated/0/Download")
		print(i,":",st)

def mp4( ):
	print("Mp4  files\t\t : \t\tsize")
	all_files = os.listdir("/storage/emulated/0/Download")
	mp4_files = [f for f in all_files  if f.endswith(".mp4")]
	times=len(mp4_files)
	print("Number of Mp4 files:",times)
	for i in mp4_files:
		st = os.path.getsize("/storage/emulated/0/Download")
		print(i,":",st)
	pass
	
def pdf( ):
	print("pdf files\t\t : \t\tsize")
	all_files = os.listdir("/storage/emulated/0/Download")
	pdf_files = [f for f in all_files  if f.endswith(".pdf")]
	times=len(pdf_files)
	print("Number of pdf files:",times)
	for i in pdf_files:
		st = os.path.getsize("/storage/emulated/0/Download")
		print(i,":",st)

def txt( ):
    print("txt files\t\t : \t\tsize")
    all_files = os.listdir("/storage/emulated/0/Download")
    txt_files = [f for f in all_files  if f.endswith(".txt")]
    times=len(txt_files)
    print("Number of pdf files:",times)
    for i in txt_files:
    	st = os.path.getsize("/storage/emulated/0/Download")
    	print(i,":",st)
				
# main function
print("1. Mp3\n2. Mp4\n3. PDF\n4. txt")
select_options ={
	  '1':mp3,
	  '2':mp4,
	  '3':pdf,
	  '4':txt}
choice=input("Enter File type:")
if select_options.get(choice):
	select_options[choice]()
else:
	sys.exit()