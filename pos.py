# Import spacy and English models
import spacy
nlp = spacy.load('en')

def read_file(filename):
	f = open(filename, "rb")
	return [line.strip() for line in f]

def main():
	sentences = read_file('notes.txt')
	sent0 = sentences[0]
	sent1 = sentences[1]
	sent2 = sentences[2]

	sent0 = nlp(unicode(sent0, "utf-8"))
	sent1 = nlp(unicode(sent1, "utf-8"))
	sent2 = nlp(unicode(sent2, "utf-8"))
	print("\n*********** Part of Speech tagging ***********\n")
	print 'Sentence 0:', sent0
	# For each token, print corresponding part of speech tag
	for token in sent0:
	    print('{} - {}'.format(token, token.pos_))
	print '-------------'
	print 'Sentence 2:', sent2
	# For each token, print corresponding part of speech tag
	for token in sent2:
	    print('{} - {}'.format(token, token.pos_))    
	
	print '=========Noun Extraction============'
	print 'Sentence 1:', sent1
	print([chunk for chunk in sent1.noun_chunks])

if __name__ == '__main__':
	main()