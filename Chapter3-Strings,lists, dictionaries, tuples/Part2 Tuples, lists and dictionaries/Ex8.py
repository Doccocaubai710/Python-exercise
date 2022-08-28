def dictionary_convert(s):
    counts=dict()
    for word in s:
        counts[word] = counts.get(word, 0) + 1
    return counts