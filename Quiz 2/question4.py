poem_lines = []

while True:
	poem = input("Write a line of your poem. Enter 'The End' when you're done. ")
	poem_split = poem.split()
	poem_lines.append(poem_split)
	
	if poem == "The End":
		break

def longest_line_wordcount(matrix):
	longest_line = ""
	for row_index in range(0,len(matrix)-1):
		if len(longest_line) < len(matrix[row_index]):
			longest_line = matrix[row_index]
	return len(longest_line)

wordcount = longest_line_wordcount(poem_lines)

print(f"The wordcount for the longest line is {wordcount}")
                                                      
                                                      
def line_comparison(matrix):
	duplicate_lines = []
	for line in matrix: 
		if line in duplicate_lines:
			return True
		duplicate_lines.append(line)
	
	return False

if line_comparison(poem_lines):
	print("Not all lines are unique")

else: 
	print("All lines are unique.")
	

def word_comparison(matrix): 
    duplicate_words = []
    for line in matrix: 
        words = line.split()
        for word in words:
            if word in duplicate_words:
                return True
            duplicate_words.append(word)
    return False

if word_comparison(poem_lines):
	print("There are duplicate words in the poem.")
else:
	print("There are no duplicate words.")