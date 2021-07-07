eng_v2 = {'a': 'æ', 'b': 'ნ','c': 'ເ','d': 'ð','e': 'ε','f': 'F','g': 'פ','h': 'H',
        'i': 'í', 'j': 'し','k': 'k','l': 'ł','m': 'ო','n': 'η','o': 'θ','p': 'ρ',
        'q': 'æ', 'r': 'າ','s': 'S','t': 'π','u': 'ש','v': 'ປ','w': 'ώ','x': 'א',
        'y': 'ү','z': 'ک', ',':',','!':'¡','.':'.','\n':'\n', '\'':'\''
}

text = '''according to all known laws of aviation, there is no way a bee should be able to fly.
Its wings are too small to get its fat little body off the ground.
The bee, of course, flies anyway because bees don't care what humans think is impossible.
Yellow, black. Yellow, black. Yellow, black. Yellow, black.
Ooh, black and yellow!
Let's shake it up a little.'''.lower().split(' ')

lst = [''.join([eng_v2[ch] for ch in word if ch != '\n']) for word in text]

print(' '.join(lst))

