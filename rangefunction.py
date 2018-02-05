
# range(start,stop,step size). step size defaults to 1 if not provided.
print(range(10))
print(list(range(10)))
print(list(range(3,9)))
print(list(range(2, 20, 3)))

# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz']
count = len(genre)
print(count)

# iterate over the list using index using while
i = 0
while i < count:
    print(genre[i])
    i += 1

# iterate over the list using index using for
for i in range(len(genre)):
	print("I like", genre[i])
