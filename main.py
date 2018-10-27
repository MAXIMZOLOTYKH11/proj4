while True:
    play = input('Start the game: ')
    if play == "Yes":
        text = str(input('Enter text in russian language: '))
        letter = str(input('Enter letter: '))
        v_letter = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
        c_letter = 'бвгджзйклмнпрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ'
        signs = ' !"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
        word = []
        translate = []
        for symbol in text:
            if symbol in signs:
                word = symbol
            elif symbol in v_letter:
                word = symbol + letter + symbol.lower()
            elif symbol in c_letter:
                word = symbol
            translate += word
        print("".join(translate))
    else:
        print('Goodbye!!!')
        break