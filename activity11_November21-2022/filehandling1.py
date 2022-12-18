fname =  input("Enter file name: ")
fh = open(fname)
text = fh.read()
print(text)
text = text.lower()
print(text)
words = text.split()
l =[]
for word in words:
    if word not in l:
        l.append(word)
l.sort()
print(l)