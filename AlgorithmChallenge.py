
# Python3 code to demonstrate 
# Grouping Anagrams 
# using defaultdict() + sorted() + values() 

from collections import defaultdict 

  
# initializing list 

test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum'] 

  
# printing original list 

print("The original list : " + str(test_list)) 

  
# using defaultdict() + sorted() + values() 
# Grouping Anagrams 

temp = defaultdict(list) 

for ele in test_list: 

    temp[str(sorted(ele))].append(ele) 

res = list(temp.values()) 

  
# print result 

print("The grouped Anagrams : " + str(res)) 
#Output :The original list : ['lump', 'eat', 'me', 'tea', 'em', 'plum']The grouped Anagrams : [['me', 'em'], ['lump', 'plum'], ['eat', 'tea']]
 
'''
Method #2 : Using list comprehension + sorted() + lambda + groupby()

The combination of above function can also be used to perform this particular task. The groupby function performs the necessary grouping together. The lambda function helps to group alike anagrams.

# Python3 code to demonstrate 
# Grouping Anagrams 
# using list comprehension + sorted() + lambda + groupby() 

from itertools import groupby 

  
# initializing list 

test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum'] 

  
# printing original list 

print("The original list : " + str(test_list)) 

  
# using list comprehension + sorted() + lambda + groupby() 
# Grouping Anagrams 

temp = lambda test_list: sorted(test_list) 

res = [list(val) for key, val in groupby(sorted(test_list, key = temp), temp)] 

  
# print result 

print("The grouped Anagrams : " + str(res)) 
Output :
The original list : ['lump', 'eat', 'me', 'tea', 'em', 'plum']
The grouped Anagrams : [['me', 'em'], ['lump', 'plum'], ['eat', 'tea']]
'''