import re
with open('data\\dataset\\input.txt', 'r') as file:
    find = re.findall(r'\b(summer)\b', file.read())
    print(len(find))