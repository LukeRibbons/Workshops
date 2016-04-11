user_string = input("Text: ")
words = user_string.split(" ")
words_keys_to_sort = []
sorted(words)
word_dictionary_count = {}
for i in range(len(words)):
    if not words[i] in word_dictionary_count:
        word_dictionary_count[words[i]] = words.count(words[i])
        words_keys_to_sort.append(words[i])
    words_keys_to_sort.sort()
for keys in words_keys_to_sort:
    print(keys, " : ", word_dictionary_count[keys])  # TODO find better way to do this
