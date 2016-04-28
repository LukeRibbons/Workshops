user_string = input("Text: ")
words = user_string.split(" ")
word_dictionary_count = {}
for word in set(words):
    word_dictionary_count[word] = words.count(word)
for key in sorted(word_dictionary_count):
    print(key, " : ", word_dictionary_count[key])
