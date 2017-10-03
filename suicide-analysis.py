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

	max_score = 0
	min_score = 1
	
	maxnote1 = ""
	maxnote2 = ""

	minnote1 = ""
	minnote2 = ""

	scores = []
	for d in docs:
		row = []
		for e in docs:
		# print docs[0]
			score = round(d.similarity(e), 3)
			
			if score > max_score and score!= 1.0:
				max_score = score
				maxnote1 = d
				maxnote2 = e


			if score < min_score and score!= 1.0:
				min_score = score
				minnote1 = d
				minnote2 = e


			row.append(score)
			

		
		scores.append(row)
	print 'Suidice Note 1:', maxnote1
	print 'Suicide Note 2:', maxnote2
	print 'Similarity Score:', max_score
	print '============================='
	print 'Suidice Note 1:', minnote1
	print 'Suidice Note 1:', minnote2
	print 'Similarity Score:', min_score

	# print scores



if __name__ == '__main__':
	main()