import collections
import string

def ceaserCipher(rotate_string, rotate_value):

    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(rotate_value)
    lower.rotate(rotate_value)
    ## rotate shifts values

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))
    ##makes list into string

    return rotate_string.translate(string.maketrans(string.ascii_uppercase, upper)).translate(string.maketrans(string.ascii_lowercase, lower))

plainText = raw_input("Enter plaintext here: ")
## Enter plaintext here for cipher text conversion
cipherText = raw_input("Enter ciphertext here: ")
##Enter Cipher Text here for plain text conversion

for i in range (len(string.ascii_uppercase)):
    print i, '|', ceaserCipher(cipherText, i) ##change plaintext to cipher text or vice versa depending on requirnment
##prints out result
