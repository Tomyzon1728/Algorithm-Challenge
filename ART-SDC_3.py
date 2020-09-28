# ART

def check_anagram(word1, word2):
   if all([x.isupper or islower in y.isupper or y.lower for x in word1 for y in word2]):
   	print("=================")
   	print("They are anagrams")
   else:
   	print("=================")
   	print("They are not anagrams")
   	
finp = input("Enter First Word:")
sinp = input("Enter Second Word:")

check_anagram(finp, sinp)
