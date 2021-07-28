# given string input , remove all vowels and then return every other letter
# remove vowels:
#   1) use regex
#   2) use set of vowels and compare elements of string if its a vowel
# return every other
#   1)s[::2]

# note:
# handle punctuation and spaces. handle upper and lower case.


def every_other(s = ''):

    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    result = ''.join([x for x in s if x not in vowels])
    return result[::2]

print(every_other('LaunchCode'))