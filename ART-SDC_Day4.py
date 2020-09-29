# ART
def freq(str):
	str = str.split()
	str2 = []
	print('word\tfrequency')
	for i in str:
	    if i not in str2:
	    	str2.append(i)
	for i in range(0, len(str2)):
		print(str2[i], '\t:', str.count(str2[i]))  
def main():
	str =input("Enter Sentence:")
	freq(str)                     
if __name__=="__main__":
	main()       