# write your code here
container = []
actual_string = ''
available_formatters = ('plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line',
                        'ordered-list', 'unordered-list')
special_commands = ('!help', '!done')

def lists(num, variant):
    variants = {'unordered-list': '*', 'ordered-list': f'{num + 1}.'}
    return f'{variants[variant]} {input(f"Row #{num + 1}:")}'

def helping():
    print(f'Available formatters: {" ".join(available_formatters)}')
    print(f'Special commands: {" ".join(special_commands)}')

def header():
    level = int(input('Level:'))
    while level not in range(1, 7):
        level = int(input('The level should be within the range of 1 to 6\nLevel:'))
    txt = input('Text:')
    string = f'{"#" * level} {txt}'
    return string

def wrap_formatter(command):
    dct = {'italic': '*', 'bold': '**', 'plain': '', 'inline-code': '`'}
    txt = input('Text:')
    string = f'{dct[command]}{txt}{dct[command]}'
    return string

def link(empty):
    label = input('Label:')
    url = input('URL:')
    string = f'[{label}]({url})'
    return string

def smart_print(string=''):
    for item in container:
        print(item)
    print(string)

inp = input('Choose a formatter:')

functions = {'plain': wrap_formatter, 'bold': wrap_formatter, 'italic': wrap_formatter,
             'inline-code': wrap_formatter, 'link': link}

with open('output.md', 'w') as file:
    while inp != special_commands[1]:
        if inp not in available_formatters and inp not in special_commands:
            print('Unknown formatting type or command')
        else:
            if inp in functions:
                content = functions[inp](inp)
                actual_string += content
                file.write(content)
                smart_print(actual_string)
            elif inp == 'new-line':
                container.append(str(actual_string))
                file.write('\n')
                actual_string = ''
                smart_print()
            elif inp == 'header':
                if actual_string:
                    container.append(str(actual_string))
                content = header()
                container.append(content)
                file.write(content+'\n')
                smart_print()
            elif inp in ('unordered-list', 'ordered-list'):
                number = int(input('Number of rows:'))
                while number <= 0:
                    print('The number of rows should be greater than zero')
                    number = int(input('Number of rows:'))
                for i in range(number):
                    content = lists(i, inp)
                    container.append(content)
                    file.write(content + '\n')
                smart_print()


        inp = input('Choose a formatter:')



