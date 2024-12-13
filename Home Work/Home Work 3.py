while True:
    word = input('Слово')
    if word == '0':
        break
    vowel = 0
    consonant = 0
    count = len(word)
    print('Количество Букв:',count)
    for letter in word:
        if letter in 'aieouyAIEOUYуеыаоэяиюУЕЫАОЭЯИЮ':
            vowel += 1
        else:
            consonant += 1
    print('Количество гласных:', vowel)
    print('Количество согласных:', consonant)



    vowel = vowel / count * 100
    vowelround = round(vowel, 2)
    consonant = consonant / count * 100
    consonantround = round(consonant, 2)
    print(f'Гласные/Согласные: {vowelround}% / {consonantround}%')

