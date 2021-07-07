# makes pyramid base 8
def pyramid(n):
    spaces = n -1
    result = ''
    for row in range(1, n):
        for space in range(spaces):
            result += ' '
        spaces -= 1
        for ch in range(row):
            result += '^ '
        result += '\n'
    return result

print(pyramid(8))

