def acronym_finder():
    ans = input('Enter a name of a person or an organizastion to find the acronym: ').lower()

    acro = [word[0] for word in ans.split() if word != 'of' and word != 'the' and word != 'at']
    print('.'.join(acro).upper())
    
if __name__ == '__main__':
    acronym_finder()