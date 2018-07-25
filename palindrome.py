import unicodedata
import sys

#function returns True if palindrome
def check_if_Palindrome(text):

    text = remove_punctuation_and_white_spaces(text)
    sentence=text.upper()
    
    rev = ''.join(reversed(sentence))
    if (sentence == rev):
        return True
    return False

def remove_punctuation_and_white_spaces(text):
	#remove panctuations
	tbl = dict.fromkeys(i for i in range(sys.maxunicode)
                      if unicodedata.category(chr(i)).startswith('P'))
	text2=text.translate(tbl)
	#return a string with no white spaces
	return text2.replace(" ", "")

#allows the code in the module to be importable by test module
#without executing the code block beneath on import.
if __name__ == "__main__":

	user_entry=[]

	for i in range(5):
		user_input = input("Type a word to check if it's a palindrome: ")
		user_entry.append(user_input)
		if check_if_Palindrome(user_input):
			print (user_input+" is a palindrome!")
			break
		else:
			print (user_input+" is not a palindrome, Try again: ")
	print (user_entry)