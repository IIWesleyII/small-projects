def typist(s):
    key_strokes = 0
    caps_lock = False
    char_dict = {'!','@','#','$','%','^','&','*','(',')','-',
                '"',':','?','<','>','|','~','{','}','+' }
    for x in s:
        if x in char_dict:
            key_strokes += 1  
        elif caps_lock:
            if x.islower():
                caps_lock = False
                key_strokes += 1
        else:
            if x.isupper():
                caps_lock = True
                key_strokes += 1
        key_strokes += 1
        
    return key_strokes
    
s = '%$'
print(typist(s))


