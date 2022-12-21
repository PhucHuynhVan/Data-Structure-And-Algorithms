
def anagram_check(str_1: str, str_2: str) -> bool:
    str_1 = str_1.replace(" ", "").lower()
    str_2 = str_2.replace(" ", "").lower()

    cnt = {}
    # Calculating the number of appearances of a character in str_1
    for letter in str_1:
        if letter in cnt:
            cnt[letter] += 1
        else:
            cnt[letter] = 1
    # Checking whether the character is in str_2 or not?
    for letter in str_2:
        if letter in cnt:
            cnt[letter] -= 1
        else:
            cnt[letter] = 1
    # Incase
    for k in cnt:
        if cnt[k] != 0:
            return False
    return True
