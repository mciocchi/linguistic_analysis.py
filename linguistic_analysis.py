# linguistic_analysis.py
# by Matt Ciocchi
# last updated 2/19/2013

def getwordfrequencies(textfield):
	"""
	getwordfrequencies is designed to take in a string and output a list of dictionaries recording each unique word, and how many times it's used. 

	for instance:

	getwordfrequencies('foo foo bar')

	will return:

	[{'word': 'foo', 'word_count': 2}, {'word': 'bar', 'word_count': 1}]
	"""

#	Turn text field into a list of words:
	textfield= textfield.split()

#	Convert the list into a set to filter out all but one instance of each unique word.
#	Afterwards, convert the set back into a list in order to be able to iterate through it.
	lexicon= list(set(textfield))

	word_frequencies= []

#	Iterate through each word in the list of words:
	for word in lexicon:

#		define a function to check the word against another arbitrary word to see if they match.
		matchesword= lambda otherword : word == otherword

#		Use map() to try to match word to every other word in the text field.
#		Filter out negatives, and count the number of positive matches to deduce the frequency of each word.
		word_count= len(filter(bool, map(matchesword, textfield)))

#		The following should associate words and word counts as key/value pairs in a dictionary:
		word_frequencies.append({'word':word,'word_count':word_count,})

#	return a list of dictionaries of words and word counts, e.g.: 
#       [{'word': 'foo', 'word_count': 2}, {'word': 'bar', 'word_count': 1}]
	return word_frequencies
