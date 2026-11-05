sentence = " the cat sat on the mat "

count = {}

for word in sentence.split():
    count[word] = count.get(word,0) + 1

print(count)
