import spacy

nlp = spacy.load('en')

def main():
	v_list = []
	docs = []
	f = open("suicide_notes.txt","r")
	for line in f.readlines():
		line = unicode(line, "utf-8")
		doc = nlp(line)
		docs.append(doc)

	# s1 = nlp(u'We had a death pact, and I have to keep my half of the bargain.')
	# s2 = nlp(u'Dear World, I am leaving because I am bored.')
	for d in docs:
		# print docs[0]
		print d
		print docs[0].similarity(d)
		print '======'

	# print docs[0].similarity(docs[0])

	# print docs[1].similarity(docs[1])
	# print s1.similarity(s2)


if __name__ == '__main__':
	main()