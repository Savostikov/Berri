name = 'Alice'
age = 18
if name == input('your name?:'):
    print('Hello Alice')
elif age < 18:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you? Alice is not undead, immortal vampire.')
else:
    print('Fuck')
