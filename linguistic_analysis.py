def getwordfrequencies(textfield):
	word_frequencies= {}

#	Turn text field into a list of words:
	textfield= textfield.split()
	lexicon= list(set(textfield))

#	Iterate through each word in the list of words:
	for word in lexicon:

#		define a function to check the word against another arbitrary word to see if they match.
		matchesword= lambda otherword : word == otherword

#		Use map() to try to match word to every other word in the text field.
#		Filter out negatives, and count the number of positive matches to deduce the frequency of each word.
		word_count= len(filter(bool, map(matchesword, textfield)))

#		The following should associate words and word counts as key/value pairs in a dictionary:
		word_frequencies.update({word : word_count,})

#	return dictionary of words and word counts, e.g. {'foo':3, 'bar': 4, 'foobar': 5,}
	return word_frequencies
