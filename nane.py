name = 'Mary'
password = 'swordfish'
if name == input('your name?:'):
    print('Hello Mary')
    if password == input('password:'):
     print('Access granted.')
    else:
     print('Wrong password')

else:
    print('User not registered') 
