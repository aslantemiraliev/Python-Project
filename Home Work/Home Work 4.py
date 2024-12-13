data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for item in data_tuple:
    if isinstance(item, str):
        letters.append(item)
    else:
        numbers.append(item)

numbers. remove (6.13)
deleted = numbers.pop (0)
letters.append(deleted)
numbers.insert(1, 2)
numbers. sort()
letters. reverse()
del letters[1]
del letters [6]
letters. insert (1, 'G')
letters. insert (7, 'c')
squared_numbers = []
for num in numbers:
     squared_numbers.append (num ** 2)
print(tuple(letters))
print (tuple(squared_numbers))