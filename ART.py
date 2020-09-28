#Day2 ∆®T 
def add_tags():
	tag=input("tag name:")
	word=input("tag item:")
	tag_2= input("tag name:")
	word_2 = input("tag item:")	
	print("\t<%s>\n\n\t%s\n\n\t</%s>\n" % (tag, word, tag))
	print("\t<%s>\n\n\t%s\n\n\t<%s>"%(tag_2,word_2,tag_2))
add_tags( )
