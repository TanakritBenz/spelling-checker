import sys, string, re, queue 

dictionary = open("words.txt", 'r')
# knownWords = {word.strip().lower() for word in dictionary}
knownWords = dict()
for word in dictionary:
    w = word.strip().lower()
    knownWords[w] = {w[i:i+2] for i in range(0, len(w))}

def main():
    while(True):
        word = input("> ").lower()
        if (len(word) == 1) or (word in knownWords):
            print(word)
            # break
        else:
            bigramSet = {word[i:i+2] for i in range(0, len(word))}
            consonants = [letter for letter in word if letter not in 'aeiou']
            consonants = unrepeated_list(consonants)
            candidates = dict()
            answer = ''
            maxjcoef = -1
            for knownWord in knownWords:
                if len(word) >= len(knownWord):
                    jCoef = find_jaccard_coefficient(bigramSet, knownWord)
                    if 0.20 <= jCoef:
                        temp = check_similar_consonants(consonants, knownWord)
                        if temp != None:
                            candidates[temp] = jCoef
                            if maxjcoef < jCoef:
                                maxjcoef = jCoef
                                answer = temp



            print(answer)
            print(candidates)
            # ls = ['sheep','people','inside','job','wake','conspiracy']
            # print(ls in candidates)
            # print('conspiracy: ' + (str)(candidates['conspiracy']))
            # print('unspicy: ' + (str)(candidates['unspicy']))

def find_jaccard_coefficient(bgs, kw):
    union = bgs.union(knownWords[kw])
    intersect = bgs.intersection(knownWords[kw])
    return len(intersect)/len(union)

def check_similar_consonants(consonants1, kw):
    consonants2 = [letter for letter in kw if letter not in 'aeiou']
    consonants2 = unrepeated_list(consonants2)
    if consonants1 == consonants2:
        return kw
    return None

def unrepeated_list(ls): 
    seen = set()
    return [ele for ele in ls if ele not in seen and not seen.add(ele)]

main()