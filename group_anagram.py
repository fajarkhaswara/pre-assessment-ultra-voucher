def group_anagrams(arr):
    anagrams = {}

    for word in arr:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]


    result = []
    for group in anagrams.values():
        result.append(group)

    return result

arr = ['cook', 'save', 'taste', 'aves', 'vase', 'state', 'map']
print(group_anagrams(arr))