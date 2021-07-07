def word_count():
    response = input('Describe yourself : ')
    count = len(response.split())
    print(f'Yikes all it takes is {count} words to describe you?  Find a hobby.')

if __name__ == '__main__':
    word_count()