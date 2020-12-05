keywords = open("keywords.txt", 'r+')
happines = 0
for words in keywords:
    words = words.strip("\n")
    words = words.split(",")
    print(words)
