def is_palindrom(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

print(is_palindrom("naman"))
print(is_palindrom("horse"))
# sushant
