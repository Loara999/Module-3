def single_root_words(root_word: str, *other_words):
    same_words = []
    i_ = ''
    root_word = root_word.lower()
    for i in other_words:
        i_ = i
        if isinstance(i, str):
            i = i.lower()
        if root_word in i or i in root_word:
            same_words.append(i_)
    return same_words


print('Однокоренные слова:', single_root_words('Disablement', \
                                               'able', 'ABLE', 'aBle'))
print('Однокоренные слова:', single_root_words('rich', 'richiest', \
                                               'orichalcum', 'cheers', 'richies'))
