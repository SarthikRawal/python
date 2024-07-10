# 9. Check for vowel or consonant
VOWEL = "aeiouAEIOU"
def vowel_consonant(char):
    if char.isdigit():
        return "enter an alphabet..!"
    if char in VOWEL:
        return f"{char} is a Vowel"
    else:
        return f"{char} is a Consonant"
    
if __name__ == '__main__':
    alphabet = input("Enter an alphabet: ")
    print(vowel_consonant(alphabet))