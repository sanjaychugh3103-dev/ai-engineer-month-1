word1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_anagrams(words):
    hashmap = {}
    for word in words:
        fingerprint = "".join(sorted(word))
        if fingerprint in hashmap:
            hashmap[fingerprint].append(word)
        else:
            hashmap[fingerprint] = [word]
    return list(hashmap.values())
    

print(group_anagrams(word1))


