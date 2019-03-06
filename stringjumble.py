"""
stringjumble.py
Author: Esther Hacker
Credit: N/A

Assignment: String Jumble

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

text = input("Please enter a string of text (the bigger the better): ")
print('You entered "' + text + '". Now jumble it: ')

#this is the first part of the problem, where all of the letters are in reverse
textlist = list(text)

reversetextlist = textlist[::-1]
reversetext = ''.join(reversetextlist)

print(reversetext)


#this is the second part, where the words are in reverse but the letters within each word are in order.
textlist2 = list(text.split())

reversetextlist2 = ' '.join(textlist2[::-1])
print(reversetextlist2)


#this is the third part, where all the words are in order but the letters within each word are reversed
textlist3 = list(text.split())

for x in textlist3:
    print(''.join(list(x[::-1])), end=" ")
