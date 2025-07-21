import nltk
from nltk import ne_chunk, pos_tag, word_tokenize, sent_tokenize

input = "I am not feeling well today. This is because i enjoyed too much during this weekend "
ner = ne_chunk(pos_tag(word_tokenize(input)))
print(ner)

from nltk.tree import Tree
named_entity = []
for subtree in ner:
    if isinstance(subtree, Tree):
        entity = (subtree.label(), ' '.join([word for word, pos in subtree.leaves()]))
        named_entity.append(entity)
print(named_entity)

import spacy
nlp = spacy.load("en_core_web_sm")

text = "Barack Obama went as a prime minister of USA in the year of 2015 . PM MODI is the prime minister of INDIA."
doc = nlp(text)
named_entity = []
for ent in doc.ents:
    named_entity.append(ent.text)
print(named_entity)