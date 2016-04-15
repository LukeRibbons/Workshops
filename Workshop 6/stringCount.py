user_string = input("Text: ")
words = user_string.split(" ")
word_dictionary_count = {}
for i in range(len(words)):
    if not words[i] in word_dictionary_count:
        word_dictionary_count[words[i]] = words.count(words[i])
for key in sorted(word_dictionary_count):
    print(key, " : ", word_dictionary_count[key])