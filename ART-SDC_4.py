# ART
import re 
sen = input("Enter sentence:")
print("Word\t\tFrequency")
m = re.sub(r'[, .]',r' ' ,sen)
wsp= m.split()
waf = {}
for word in wsp:
	if word in waf:
		waf[word] = waf[word] +1
	else:
		waf[word] = 1		
for x, y in waf.items():
	print(x, "\t\t:", y)
max_key = max(waf, key=waf.get)
all_values = waf.values()
max_value = max(all_values)
print("Highest Frequency:",max_key)
print("Number of Times:",max_value)
