from numpy import dot
from spacy.en import English
from numpy.linalg import norm
parser = English()

print(len(parser.vocab))
allWords = list({w for w in parser.vocab if w.has_vector and w.orth_.islower() and w.lower_ != "nasa"})

print allWords
# you can access known words from the parser's vocabulary

# nasa = parser.vocab['NASA']



# # cosine similarity
# cosine = lambda v1, v2: dot(v1, v2) / (norm(v1) * norm(v2))

# # gather all known words, take only the lowercased versions
# allWords = list({w for w in parser.vocab if w.has_repvec and w.orth_.islower() and w.lower_ != "nasa"})
# print(len(allWords))
# # sort by similarity to NASA
# allWords.sort(key=lambda w: cosine(w.repvec, nasa.repvec))
# allWords.reverse()
# print("Top 10 most similar words to NASA:")
# for word in allWords[:10]:   
#     print(word.orth_)