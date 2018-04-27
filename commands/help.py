def send_help(message):
    return 'Howdy {0.author.mention}, these are the things I can do right now \n\n' \
           '!hello\t\t\t I can say hello to you \n'\
           '!welcome\t\t\t I can send you a warm welcome! \n'\
           '!features\t\t\t Show feature requests you lunatics have made \n' \
           '!wink\t\t\t ;) \n' \
           '!peekaboo\t\t\t You are in for a big surprise... \n' \
           '!gaming\t\t\t I will send you a picture of me gaming \n' \
           '!k\t\t\t K'.format(message)
