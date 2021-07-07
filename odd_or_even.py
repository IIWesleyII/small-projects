def odd_even():
    exit = False
    while exit == False:
        try:
            print('--------------------------------------------------------------------------------------------')
            print('Enter a number to find out if it\'s even or odd!'
                    + ' Or type exit to exit program.')
            response = input('\nEnter a number : ')
            if str(response).lower() == 'exit':
                print('Thanks for playing! Goodbye.')
                exit = True
                break
            if int(response) % 2 == 0:
                print(str(response) + ' is even!\n')
            else:
                print(str(response) + ' is odd!\n')
        except:
            print('ERROR, please enter valid number.\n')

if __name__ == '__main__':
    odd_even()
