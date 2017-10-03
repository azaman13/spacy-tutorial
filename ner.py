# Import spacy and English models
import spacy
nlp = spacy.load('en')

def read_file(filename):
	f = open(filename, "rb")
	return [line.strip() for line in f]

def main():
	sentences = read_file('notes.txt')
	sent1 = sentences[0]
	sent2 = sentences[1]
	sent1 = nlp(unicode(sent1, "utf-8"))
	sent2 = nlp(unicode(sent2, "utf-8"))
	print("\n*********** NER ***********\n")
	print 'Sentence 1:', sent1
	# For each token, print corresponding part of speech tag
	for ent in sent1.ents:
		print('{} - {}'.format(ent, ent.label_))

	print '====================='
	print 'Sentence 2:', sent2
	for ent in sent2.ents:
		print('{} - {}'.format(ent, ent.label_))

if __name__ == '__main__':
	main()