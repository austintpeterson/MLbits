#correctly learning nltk?

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer



#get it all baby
#nltk.download()

sample_text = "Hello there Austin, how are you doing today?  The weather is nice out."
example_sent = "This is an example of a sentence that shows off stop word filtering"

stop_words = set(stopwords.words("english"))#mod for appl.

stem_words = ["python","pythoner","pythoning","pythoned","pythonly"]

#part of speech tagging
train_speech = state_union.raw("2005-GWBush.txt")
sample_speech = state_union.raw("2006-GWBush.txt")






def main():
	ans = True

	while ans:
		ans=input("Select menu item.\n")
		
		if ans=="1":
			print("1:\n")
			#tokenizing
			print(sent_tokenize(sample_text))
			print(word_tokenize(sample_text))

		elif ans =="2":
			print("2:\n")

			#stopwords
			words = word_tokenize(example_sent)
			filtered_sent = []
			for w in words:
				if w not in stop_words:
					filtered_sent.append(w)

			print(filtered_sent)

		elif ans =="3":
			print("3:\n")

			#stemming
			ps = PorterStemmer()

			for w in stem_words:
				print(ps.stem(w))
			#need wordnet

		elif ans =="4":
			print("4:\n")

			GWsent_tok = PunktSentenceTokenizer(train_speech)

			tokenized = GWsent_tok.tokenize(sample_speech)

			for i in tokenized:
				words = nltk.word_tokenize(i)
				#add stemming beforehand?
				tagged = nltk.pos_tag(words)

				print(tagged)

		#4 but better
		elif ans =="5":
			print("5:\n")
			
			#take GW speech, tokenize sentences, throw out stopwords, stem words, tag

			#tokenize sentence w/ custom tokenizer
			GWsent_tok = PunktSentenceTokenizer(train_speech)
			tokenized = GWsent_tok.tokenize(sample_speech)

			for i in tokenized:
				print(i)

				words = nltk.word_tokenize(i)

				filtered_sent = []
				#stopword tossing
				for w in words:
					if w not in stop_words:
						filtered_sent.append(w)

				ps = PorterStemmer()

				stemd_sent = []
				#stem word reduction
				for w in filtered_sent:
					stemd_sent.append(ps.stem(w))

				tagged = nltk.pos_tag(stemd_sent)

				print(tagged)
				print("\n\n")







		elif ans =="q":
			ans = False

		else:
			print("bad input\n")

main()






































