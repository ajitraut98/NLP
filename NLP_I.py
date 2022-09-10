# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:00:45 2022

@author: AJIT
"""

### natural-language-processing
  		
## remove punctuation
  
from string import punctuation
text = text.translate(punctuation)
  			
## convert words to lower or upper case
  
text = text.lower()
text = text.upper()
  
## tokenize text

# tokenize text into different words
from nltk.tokenize import word_tokenize
words = word_tokenize(text)

# tokenize text into different sentences
from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(text)

# tokenise text into different words - tokenizes emojis, hashtags and other social media elements properly
from nltk.tokenize import TweetTokenizer
tokenizer = TweetTokenizer()
tokenizer.tokenize(text)

# tokenise words and return words that match the regex pattern
from nltk.tokenize import regexp_tokenize
regexp_tokenize(text, pattern)

## plot word frequencies and word lengths

from nltk import FreqDist
from collections import Counter
import seaborn as sns
import requests

# download text
url = "https://www.gutenberg.org/files/11/11-0.txt"
book = requests.get(url)
text = book.text

# plot word frequencies
def plot_word_frequency(words, top_n=10):
    word_freq = FreqDist(words)                # or word_freq = Counter(text)
	words = [element[0] for element in word_freq.most_common(top_n)]
	frequencies = [element[1] for element in word_freq.most_common(top_n)]
	plot = sns.barplot(words, frequencies)
    return plot
plot_word_frequency(word_tokenize(text))

def plot_word_length(words):
	word_lengths = [len(word) for word in words]
	plt.hist(word_lengths)
plot_word_length(word_tokenize(text))

## strip whitespace from words

words = [word.strip() for word in words]

## remove stopwords

from nltk.corpus import stopwords
stops = stopwords.words('english')
words = [word for word in words if word not in stops]

## spell correction
 
from spell_corrector import rectify
words = [rectify(word) for word in words]

## stemming and lemmatization

# stemming

# porter stemmer - works only on english words
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
words = [stemmer.stem(word) for word in words]

# snowball stemmer - works on english words (better than porter) as well as some foreign language words
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
words = [stemmer.stem(word) for word in words]

# lemmatization

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words = [lemmatizer.lemmatize(word) for word in words]

## bag-of-words model

documents = ["This is document one.",
			 "This is document two. A document can contain multiple sentences!",
			"This is the third document. :)"]

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
bow_model = vectorizer.fit_transform(documents)
			
# print sparse matrix
print(bow_model)

# print full matrix
print(bow_model.toarray())

# convert matrix to dataframe
bow_model = pd.DataFrame(bow_model.toarray(), columns = vectorizer.get_feature_names())

## tf-idf model

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
tfidf_model = vectorizer.fit_transform(documents)
		
# print sparse matrix
print(tfidf_model)

# print full matrix
print(tfidf_model.toarray())

# convert matrix to dataframe
tfidf_model = pd.DataFrame(tfidf_model.toarray(), columns = vectorizer.get_feature_names())

## text preprocess function

def clean_document(document, remove_punct=True, sentence_case="lower", remove_stops=True, 
                   spell_correction=False, stem=True, min_word_length=0, char_filter = r"[^\w]"):
 '''
input:
	document          :  string
  	remove_punct      :  whether to remove all the punctuations from the document
   	sentence_case     :  change document to "lower" case, "upper" case, or keep "same" case as provided
   	remove_stops      :  whether to remove stopwords from document
   	spell_correction  :  whether to correct spelling of each word
   	stem              :  whether to stem each word
   	min_word_length   :  remove words shorter than min_word_length
   	char_filter       :  regex pattern - removes those characters from the text that match the pattern

output: clean document
'''

# remove all punctuations
if remove_punct:
	from string import punctuation
	document = document.translate(punctuation)
			    
# convert words to lower case
if sentence_case == "lower":
	document = document.lower()
elif sentence_case == "upper":
	document = document.upper()

# tokenise words
from nltk.tokenize import word_tokenize
words = word_tokenize(document)
			    
# strip whitespace from all words
words = [word.strip() for word in words]

# remove stopwords
if remove_stops:
	from nltk.corpus import stopwords
	stops = set(stopwords.words("english"))
    words = [word for word in words if word not in stops]

# spell correction
if spell_correction:
	from spell_corrector import rectify
	words = [rectify(word) for word in words]
				
# stemming
if stem:
	from nltk.stem.snowball import SnowballStemmer
	stemmer = SnowballStemmer('english')
	words = [stemmer.stem(word) for word in words]

# remove extremely short words
words = [word for word in words if len(word) > min_word_length]

# join back words to get document
document = " ".join(words)

# remove unwanted characters
import re
document = re.sub(char_filter, " ", document)       # compile regex for quick processing

# replace multiple whitespaces with single whitespace
document = re.sub(r"\s+", " ", document)

# strip whitespace from document
document = document.strip()
		return document		
		
## edit-distance

from nltk.metrics.distance import edit_distance
edit_distance("hello", "hola", substitution_cost=1, transpositions=True)

## named-entity recognition (NER) using spacy

import spacy
			
nlp = spacy.load("en")                            # load english corpus
print(npl.entity)
			
doc = nlp("sample text")                          # NER
print(doc.ents)                                   # look at entities
			
# print entities
for entity in doc.ents:
	print(entity.text, entity.label_)             # look at entities and their labels

==============================================================================================================================