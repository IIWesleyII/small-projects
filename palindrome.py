# check if list item is palindrome
polly = ['walaw','racecar','cheeseburger','HI! Welcome to Chilis!', 78.3, 'wow','a', ' ', ' wow' ]

def palindrome(lst):
    file = open('results/palindrome.txt','a')
    for item in lst:
        if type(item) == str and item.strip() == item[::-1].strip():
            file.write(item + '\n')
    print('File complete')
    file.close()
    
if __name__ == '__main__':
    palindrome(polly)

