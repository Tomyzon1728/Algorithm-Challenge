def longest_word(word_char):  
    longest_word = ''  
    size = 0   
    for word in word_char:
        if len(word) > size:
        	longest_word = word
        	size = len(word)      
    print("longest word:",longest_word)
    print("letters:",size)

words = input('Enter your preferred sentence:'  )
word_char= words.split()  
longest_word(word_char)