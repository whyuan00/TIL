words = ('h', 'e', 'l', 'p')
words_list = list(words)
words_list = [char if char != 'p' else 'l'for char in words_list]
print(words_list)
words = tuple(words_list)
print(words)