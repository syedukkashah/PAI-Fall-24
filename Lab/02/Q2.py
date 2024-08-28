def is_vowel(a):
    return a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u'


word = "python"

print("Checking if ", word, "last word is vowel\n", is_vowel(word[-1]))


