import nltk
nltk.download('words', quiet=True)
nltk.download('names', quiet=True)
from nltk.corpus import words, names
import re
def encrypt(text,shit_num):
    """
    This function encrypt a given text with small and capital letter also with numbers

    Args:
        text:String
        shit_num : Integer

    Returns:
        An enrypted text
    """
    cipher_words = []
    words =text.split()
    for word in words:
        output=''
        for char in word:
            if ord(char)>64 and ord(char)<=90:
                output+=chr(((ord(char)+shit_num-65)%26)+65)
            elif ord(char)>96 and ord(char)<=122:
                output+=chr(((ord(char)+shit_num-97)%26)+97)
            elif ord(char)>48 and ord(char)<=57:
                output+=str((int(char)+shit_num)%10)
        cipher_words.append(output)
    return ' '.join(cipher_words)

def decrypt(text,shit_num):
    """
    This function decrypt a given text with small and capital letter also with numbers

    Args:
        text:String
        shit_num : Integer

    Returns:
        An enrypted text
    """
    return encrypt(text,- shit_num)
    
def crack(text):
    """
    This function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.

    Args:
        text:String

    Returns:
        original state message: String
    """
    words_list = words.words()
    names_list = names.words()

    word_collection = []
    for i in range(26):
        word_collection.append(decrypt(text, i))

    for phrase in word_collection:
        phrase_arr = phrase.split(" ")
        word_count = 0
        for word in phrase_arr:
            word=re.sub(r'[^A-Za-z]','',word)
            if word.lower() in words_list or word.lower() in names_list:
                word_count += 1
            
        total_words = len(phrase.split(" "))
        ratio = word_count / total_words
        percentage = ratio * 100
        threshold = 80

        if percentage > threshold:
            output=f'{(" ").join(phrase_arr)}, percentage:{percentage}%'

    return output





if __name__ == "__main__":

    print(encrypt('majed',15))
    print(crack('Sd gkc dro locd yp dswoc sd gkc dro gybcd yp dswoc'))