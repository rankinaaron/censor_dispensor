# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#censors a string and preserves formatting
def censor_phrase(phrase):
	censored_phrase = ''
	for char in phrase:
		if char == ' ':
			censored_phrase += ' '
		elif char == ',':
			censored_phrase +=  ','
		elif char == '.':
			censored_phrase += '.'
		elif char == '!':
			censored_phrase += '!'
		else:
			censored_phrase += '*'
	return censored_phrase

#searches text for a given phrase and censors it
def censor_text(phrase, input_text):
	censored_text = input_text.replace(phrase, censor_phrase(phrase))
	censored_text = censored_text.replace(phrase.title(), censor_phrase(phrase))
	censored_text = censored_text.replace(phrase.upper(), censor_phrase(phrase))
	return censored_text

#print(censor_text('learning algorithms', email_one))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "herself", "her"]

#a simple solution to censor a list of phrases. Erroneously censors words contained in other words i.e. "researc***s"
def censor_list(list_of_phrases, input_text):
	for phrase in list_of_phrases:
		input_text = censor_text(phrase, input_text)
	return input_text

#print(censor_list(proprietary_terms, email_two))

negative_words = ["concerned", "behind", "dangerous", "danger", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]

#simple solution to censor negative words, misses censoring multi-word phrases
def censor_negative(list_of_phrases, negative_words, input_text):
	input_text = censor_list(list_of_phrases, input_text)
	count = 0
	censored_text = []
	for word in input_text.split():
		for bad_word in negative_words:
			if word == bad_word:
				count += 1
		if count > 2 and word.strip(' ,.').lower() in negative_words:
			censored_text.append(censor_phrase(word))
		else:
			censored_text.append(word)
	return ' '.join(censored_text)

#robust solution for censoring negative words after first 2 ocurrences
def censor_neg_full(list_of_phrases, negative_words, input_text):
	input_text = censor_list(list_of_phrases, input_text)
	indeces = []
	for phrase in negative_words:
		if phrase in input_text:
			indeces.append(input_text.find(phrase))
	indeces.sort()
	uncensored = input_text[0: indeces[2]-1]
	censored = censor_list(negative_words, input_text[indeces[2]:-1])
	return uncensored+' '+censored



	
print(censor_neg_full(proprietary_terms, negative_words, email_three))
	



	#if censored_text.count()
#censors all phrases in list_of_phrases
#def censor_list_of_phrases(list_of_phrases, input_text):
#	for index, word in enumerate(censored_text):
#		if input_text[input_text.find(list_of_phrase[index])-1] != ' '

	
#print(email_two.find('personality matrix')-1)
#print(censor_list_of_phrases(proprietary_terms, email_two))





#def censor_phrase(phrase_to_censor, raw_text):
#	delineated_text = text_delineate(raw_text)
#	censored_text = []
#	if ' ' in phrase_to_censor:
#		delineated_phrase = text_delineate(phrase_to_censor)
#		censored_delineated_phrase = []
#		for text_index in range(len(delineated_text)):
#			if delineated_text[text_index] == delineated_phrase[0]:
#				for i in range(len(delineated_phrase)):
#					if delineated_text[text_index+i] == delineated_phrase[i]:
#						censored_delineated_phrase.append(bleep(delineated_phrase[i]))
#				censored_text.append(censored_delineated_phrase)
#	else:
#		for word in delineated_text:
#			if word == phrase_to_censor or word.lower() == phrase_to_censor:
#				censored_text.append(bleep(word))
#			elif word.strip(',.!') == phrase_to_censor:
#				censored_text.append(bleep(word.strip(',.!')))
#			else:
#				censored_text.append(word)
#	print(censored_text)
#
#
#print(censor_phrase('learning algorithms', email_one))
				


#def censor_text(word_to_censor, delineated_text):
#	censored_text = []
#	for index in range(len(text)):
#		if delineated_text[index] == word_to_censor or delineated_text[index].lower() == word_to_censor



#	if ' ' in word_to_censor:

#	return input_text.replace(word_to_censor, len(word_to_censor)*'*')

#print(censor_text('learning algorithms', email_one))
#proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

#print(text_delineate(email_two))

#def censor_list_of_terms(terms_to_censor, text_list):
#	censored_text = []
#	for word in text_list:
#		for term in terms_to_censor:
#			if word == term or word.lower() == term:

#def 
#def censor_list_of_terms(terms_to_censor, input_text):
#	input_text_list = input_text.split()
#	censored_text = []
#	for term in input_text_list:
#		for censor_term in terms_to_censor:
#			if censor_term == term or censor_term == term.lower():
#				censored_text.append('*'*len(term))
#		censored_text.append(term)
#	return " ".join(censored_text)

#print(censor_list_of_terms(proprietary_terms, email_two))



#def censor_list_of_terms(list_of_terms, input_text):
	

#def censor_list_of_text(word_list, input_text):
#	for term in word_list:
#		censored_word_text = input_text.replace(term, '*'*len(term))
#		input_text = censored_word_text
#	return censored_word_text

#print(censor_list_of_text(proprietary_terms, email_two))