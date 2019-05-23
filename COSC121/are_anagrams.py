def are_anagrams(word1, word2):
    """Returns true or not"""
    if word1 == word2:
        return False
    elif word1 != word2:
        word1list = list(word1)
        word2list = list(word2)
        word1list.sort()
        word2list.sort()
        if word1list == word2list:
            return True
        elif word1list != word2list:
            return False
    