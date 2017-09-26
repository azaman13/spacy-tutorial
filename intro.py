
# Import spacy and English models
import spacy

nlp = spacy.load('en')


# Process the sentences 
#         'Hello, world. Natural Language Processing in 10 lines of code.' using spaCy
print("=> This is the original sentence:")
print("Hello, world. Natural Language Processing in 10 lines of code.\n")

doc = nlp(u"Hello, world. Natural Language Processing in 10 lines of code.")


# Get first token of the processed document
token = doc[0]
print("\n=> This is the first token:")
print(token)

# Print sentences (one sentence per line)
print("\n=> Printing sentences (one sentence per line)")
for sent in doc.sents:
    print(sent)


print("\n*********** Part of Speech tagging ***********\n")
# Part of Speech taggin*

# For each token, print corresponding part of speech tag
for token in doc:
    print('{} - {}'.format(token, token.pos_))


print("\n*********** Named Entities Example ***********\n")

doc_2 = nlp(u"I went to Paris where I met my old friend Jack from uni.")
for ent in doc_2.ents:
    print('{} - {}'.format(ent, ent.label_))


print("*** \n Print noun chunks for: I went to Paris where I met my old friend Jack from uni.\n****")
# Print noun chunks for doc_2
print([chunk for chunk in doc_2.noun_chunks])


# Unigram Probabilities based on a large corpus from spacy

print("\n***\n For every token in doc_2, print log-probability of the word, \nestimated from counts from a large corpus\n****\n")
# The probability estimate is based on counts from a 3 billion word
# corpus, smoothed using the Simple Good-Turing method.
for token in doc_2:
    print(token, '=>', token.prob)


print("\n **** Word embedding based Similarity  ****  \n")

print("Example 1: The King ordered the man to remove the woman and kill his queen")

doc3 = nlp(u"The King ordered the man to remove the woman and kill his queen.")
king = doc3[1]
man = doc3[4]
woman = doc3[8]
queen = doc3[-1]
print("Similarity between king and man:",king.similarity(man))

print("Similarity between king and woman:",king.similarity(woman))

print("Similarity between king and queen:",king.similarity(queen))


print("\n \nExample 2: The King ordered the man to remove the woman and kill his queen.")

# For a given document, calculate similarity between 'apples' and 'oranges' and 'boots' and 'hippos'
doc4 = nlp(u"Apples and oranges are similar. Boots and hippos aren't.")
apples = doc4[0]
oranges = doc4[2]
boots = doc4[6]
hippos = doc4[8]
print("Apples and oranges similarity score:", apples.similarity(oranges))
print("Boots and hippos similarity score:", boots.similarity(hippos))


print("\n\n We can also do: Similarity between sentence and a word.\n")
# Print similarity between sentence and word 'fruit'
apples_sent, boots_sent = doc4.sents
fruit = doc4.vocab[u'fruit']
print("Similarity between the apple's sentence and the word ")
print(apples_sent.similarity(fruit))
print(boots_sent.similarity(fruit))

