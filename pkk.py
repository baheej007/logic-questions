def an(words):
    result = []
    seen = []

    for i in words:
        if i in seen:
            continue
        group = [i]
        seen.append(i)

        for j in words:
            if i != j and sorted(i) == sorted(j):
                group.append(j)
                seen.append(j)

        result.append(group)

    print(result)

an(["eat", "tea", "tan", "ate", "nat", "bat"])
