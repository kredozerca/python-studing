import sys

number_of_tries = 5
word = "Tygrysek"


used_letter = []
user_word = []


	
	

def find_indexes(word, letter):
	indexes = []

	for index, letter_in_word in enumerate(word):
			if letter == letter_in_word:
				indexes.append(index)
			
	return indexes
	
def show_stats():
	print()
	print(" ,".join(used_letter))
	print("Pozostalo", number_of_tries, "prób")
	print(" ".join(user_word))
	print()
	
for _ in word:
	user_word.append("_")

while True:
	letter = input("Podaj literę:")
	used_letter.append(letter)
	
	
	found_indexes = find_indexes(word, letter)
	if len(found_indexes) == 0:
		number_of_tries -= 1
		print("W szukanym wyrazie nie ma wskazanej litery")
		
		
		if number_of_tries == 0:
			print("Koniec gry!")
			sys.exit(0)
			
	else:
		for index in found_indexes:
			user_word[index] = letter
	
		if "".join(user_word)== word:
			print("Brawo, wygrałeś!")
			sys.exit(0)
			
		show_stats()