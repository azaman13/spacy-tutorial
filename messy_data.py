from spacy.en import English
parser = English()


messyData = u"lol that is rly funny :) This is gr8 i rate it 8/8!!!"
parsedData = parser(messyData)
for token in parsedData:
    print(token.orth_, token.pos_, token.lemma_)
    
# it does pretty well! Note that it does fail on the token "gr8", 
# taking it as a verb rather than an adjective meaning "great"
# and "lol" probably isn't a noun...it's more like an interjection