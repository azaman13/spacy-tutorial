def main():
	f = open("suicide_notes.txt","r")
	for line in f.readlines():
		print line

if __name__ == '__main__':
	main()