def a():
    print('a() starts')
    b()
    c()
    print('a() returns') 

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

a()   