# dCripta - part of LlamaxCripta by Llamax
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

import time,sys,string,random

print("LlamaxCripta - dCripta\n")
print("This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.")
print("To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.\n")

# Prompts for the phrase to be decrypted
text = raw_input("Enter encrypted phrase: ")

# Prompts for the keys
key1 = raw_input("Enter key 1 >>>")
key2 = raw_input("Enter key 2 >>>")

# Makes a translation table using both keys.
# See https://docs.python.org/2/library/string.html#string.maketrans for more info.
translate_table = string.maketrans(key2, key1)
# Translates the phrase using translate_table and shares it with the user
# See https://docs.python.org/2/library/string.html#string.translate for more info.
print("Encrypted phrase is:\n" + text.translate(translate_table))