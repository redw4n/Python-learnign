spam  = {'Color': 'Red', 'Age': '42'}
for x in spam.values():
    print(x)

if 'Color' in spam.keys():
    print('True')
else:
    print('Recheck Key Values')