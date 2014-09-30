import sys, random

def incorrect_vowel_helper(word, pos, letter):
    newWord = ''
    for i in range(0, len(word)):
        if i == pos:
            newWord += letter
        else:
            newWord += word[i]
    return newWord

def incorrect_vowel(word, pos, someSet):
    vowels = 'aeiou'
    for index in range(pos, len(word)):
        if word[index] in vowels:
            for v in vowels:
                newWord = incorrect_vowel_helper(word, index, v)
                incorrect_vowel(newWord, index+1, someSet)
                someSet.add(newWord)
    return someSet          

def repeat_some_letter(word):
    newWord = ''
    i = random.randint(1, len(word)-1)
    newWord = word[:i] + word[i-1] + word[i:]
    return newWord

def random_case(word):
    newWord = ''
    for i in range(0, len(word)):
        j = random.randint(0, len(word)-1)
        if (j%2) == 0:
            newWord += word[i].upper()
        else:
            newWord += word[i].lower()
    return newWord

iterCounter = 0
greeting = 'Enter a correctly spelled English word (or exit() to quit): '
while True:
    word = input(greeting).strip().lower()
    if 'exit()' in word:
        print('Quit program. Bye!')
        break
    else:
        someSet = set()
        incorrect_vowel(word, 0, someSet)
        someList1 = [repeat_some_letter(word) for word in someSet]
        someList2 = [repeat_some_letter(word) for word in someList1]
        someList3 = [repeat_some_letter(word) for word in someList2]
        someList4 = [repeat_some_letter(word) for word in someList3]
        someList5 = someList1 + someList2 + someList3 + someList4
        newList = [word] + [random_case(word) for word in someList5] + ['\n']

        with open("Generated_Words.txt", 'a') as file:
            if iterCounter == 0:
                for item in ['sheeeeep', 'peepple', 'inSIDE', 'jjoobbb', 'weke', 'CUNsperrICY', 'peeeeeoooooaaaapple', 'peeeeeeeeeeeeeeeeeeeepppppppppple', '\n']:
                    file.write("{}\n".format(item))
                iterCounter += 1
            for item in newList:
                file.write("{}\n".format(item))


