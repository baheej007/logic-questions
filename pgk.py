def group_anagrams(words):
    result = []      # Final grouped anagram lists
    visited = []     # To track already grouped words

    for i in range(len(words)):
        if words[i] not in visited:
            group = [words[i]]
            visited.append(words[i])

            for j in range(i + 1, len(words)):
                if sorted(words[i]) == sorted(words[j]):
                    group.append(words[j])
                    visited.append(words[j])

            result.append(group)

    print(result)

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
