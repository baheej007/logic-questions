from collections import defaultdict

def group_anagrams(words):
    grouped = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))
        grouped[key].append(word)

    return list(grouped.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
