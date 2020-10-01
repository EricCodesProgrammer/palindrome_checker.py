ask_pal = input('Enter text: ')

def get_pal(ask_pal):
    return ask_pal == ask_pal[::-1]

ans = get_pal(ask_pal)
if ans == True:
    print('It is a palindrome')
else:
    print('It is not a palindrome')