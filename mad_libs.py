
def mad_libs():
    result = ''
    exit = False
    while exit == False:
        try:
            print('----------------------------------------------------')
            verb_1 , verb_2 , verb_3 = input('Enter three verbs that end in \'ing\': ').split()
            adj_1, adj_2 , adj_3 = input('Enter three adjectives: ').split()

            result = f'''            So I was saying, there was this {adj_1} guy over here {verb_1}.
            He looks at me like I\'m crazy and I\'m like ayyyyy I\'m just over here {verb_2} with my {adj_2} spaghetti!
            So he\'s {verb_3} on my favorite {adj_3} table so I slapped him with a spaghetti noodle!''' 
                    
            exit = True
        except:
            print('ERROR, Please enter the correct number of words.')
    print(result)

if __name__ == '__main__':
    mad_libs()