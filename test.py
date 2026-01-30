database = [
    {
        'username': 'misha',
        'password': 'admin',
    },
    {
        'username': 'alex',
        'password': '123456',
    },
    {
        'username': 'john',
        'password': 'password2',
    }
]

def checkUsername(username):
    for user in database:
        if user['username'] == username:
            print('username found')
            return True
    print('username not found')
    return False

def checkPassword(username, password):
    for user in database:
        if user['password'] == password and user['username'] == username:
            return True
    return False

if __name__ == '__main__':
    uname = input('Enter your username: ')
    if(checkUsername(uname)):
        pword = input('Enter your password: ')
        if(checkPassword(uname ,pword)):
            print('Login successful')
        else: 
            print('Invalid password')
    else:
        print('Invalid username')