birthdays = {'Tanvir': '26th Oct', 'Taufiq': '3rd Dec', 'Rafay': '28th Nov'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
     
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birth date?')
        bday = input()
        birthdays[name] = bday 
        print('Information Updated.')