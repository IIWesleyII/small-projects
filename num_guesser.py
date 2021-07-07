class Games:
    def __init__(self, name):
        self.name = name
    def num_guesser(self):
        print(f'Hey {self.name}! Guess the number! It\'s between 1-100')
        special_num = 45
        selection = input('Select a number between 1 and 100: ')
        while True:
            if not selection.isnumeric() or int(selection) > 100 or int(selection) < 1:
                print('Please enter a valid number.')
            elif int(selection) == special_num:
                print(f'Congrats you picked the correct number: {selection}!')
                break
            elif int(selection) > special_num:
                print(f'{selection} is too high!')
            elif int(selection) < special_num:
                print(f'{selection} is too low!')
            else:
                raise Exception('Error')   
            selection = input('Select a number between 1 and 100: ')
        return f'Thanks for playing {self.name}!'
        
game_1 = Games('Wesley')

print(game_1.num_guesser())

