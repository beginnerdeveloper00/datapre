input = "Barack Obama went as a prime minister of USA in the year of 2015 . PM MODI is the prime minister of INDIA."
print(input)

from nltk import word_tokenize
word_tokens = word_tokenize(input)

#(4)Stemmer
stemming = []
from nltk import PorterStemmer
for word in word_tokens:
    stemming.append(PorterStemmer().stem(word))
print(stemming)

#(5)Lemmatizer
from nltk import WordNetLemmatizer
lma = []
for word in word_tokens:
    lma.append(WordNetLemmatizer().lemmatize(word))
print(lma)

#(6)POS Tags
from nltk import pos_tag
print(pos_tag(word_tokens))