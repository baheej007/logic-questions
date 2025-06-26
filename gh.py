def an(list):
    all = []     # Final result list
    visited = [] # Already grouped words

    for i in list:
        if i not in visited:
            data = [i]           # Temporary group
            visited.append(i)

            for j in list:
                if i != j and sorted(i) == sorted(j):
                    data.append(j)
                    visited.append(j)

            all.append(data)     # One group added to final list

    print(all)

an(["eat", "tea", "tan", "ate", "nat", "bat"])
