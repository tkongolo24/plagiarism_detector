#looking for common words
def common_words(freq1, freq2):
    common = {}
    for word in freq1:
        if word in freq2:
            common[word] = (freq1[word], freq2[word])
    return common
    

print(common_words(freq1, freq2))
