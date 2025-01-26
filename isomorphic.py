def is_isomorphic(s, t):
    mapping_s, mapping_t = {}, {}
    for i in range(len(s)):
        if mapping_s.get(s[i], t[i]) != t[i] or mapping_t.get(t[i], s[i]) != s[i]:
            return False
        mapping_s[s[i]] = t[i]
        mapping_t[t[i]] = s[i]
    return True

print(is_isomorphic("egg", "add"))
print(is_isomorphic("foo", "bar"))
