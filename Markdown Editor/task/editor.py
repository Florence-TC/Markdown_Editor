formatters = ['plain', 'bold', 'italic', 'header', 'link', 'ordered-list', 'unordered-list', 'inline-code', 'new-line']
markdown = ''


def plain():
    return input('Text: ')


def bold():
    return '**' + input('Text: ') + '**'


def italic():
    return '*' + input('Text: ') + '*'


def header():
    level = 0
    while not 1 <= level <= 6:
        print('The level should be within the range of 1 to 6')
        level = int(input('Level: '))
    else:
        return level * '#' + ' ' + input('Text: ') + '\n'


def link():
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


def ordered_list():
    nb_of_rows = 0
    while not nb_of_rows > 0:
        print('The number of rows should be greater than zero')
        nb_of_rows = int(input('Number of rows: '))
    else:
        numbers = []
        rows = []
        for i in range(nb_of_rows):
            numbers.append(f'{i + 1}. ')
            rows.append(input(f'Row #{i + 1}'))
        return list(map(lambda x, y: x + y + '\n', numbers, rows))


def unordered_list():
    nb_of_rows = 0
    while not nb_of_rows > 0:
        print('The number of rows should be greater than zero')
        nb_of_rows = int(input('Number of rows: '))
    else:
        rows = []
        for i in range(nb_of_rows):
            rows.append(input(f'Row #{i + 1}'))
        return list(map(lambda x: '* ' + x + '\n', rows))


def inline_code():
    return '`' + input('Text: ') + '`'


def new_line():
    return '\n'


while True:
    user_input = input('Choose a formatter: ')
    if user_input == '!done':
        file = open('output.md', 'w')
        file.write(markdown)
        file.close()
        break
    elif user_input == '!help':
        print('''Available formatters: plain bold italic header link ordered-list unordered-list inline-code new-line
Special commands: !help !done''')
    elif user_input in formatters:
        if user_input == 'plain':
            markdown += plain()
            print(markdown)
        elif user_input == 'bold':
            markdown += bold()
            print(markdown)
        elif user_input == 'italic':
            markdown += italic()
            print(markdown)
        elif user_input == 'header':
            markdown += header()
            print(markdown)
        elif user_input == 'link':
            markdown += link()
            print(markdown)
        elif user_input == 'inline-code':
            markdown += inline_code()
            print(markdown)
        elif user_input == 'new-line':
            markdown += new_line()
            print(markdown)
        elif user_input == 'ordered-list':
            for item in ordered_list():
                markdown += item
            print(markdown)
        elif user_input == 'unordered-list':
            for item in unordered_list():
                markdown += item
            print(markdown)
    else:
        print('Unknown formatter type or command')
