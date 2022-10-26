# We checked the passwords and user is Authenticated
# And we will authorize him...
authorized = False

def is_authorized(f):
    def decorated_function(*args, **kwargs):
        if authorized:
            f(*args, **kwargs)
        else:
            print('Not Auhtorized!')
    return decorated_function


def append_details(f):
    def decorated_function(*args, **kwargs):
        details = '-----\n'
        details += f(*args, *kwargs)
        details += '\nversion: v1.0\n'
        details += '-----\n'
        return details
    return decorated_function


@is_authorized
def list_users():
    print('Mathias\nJohn\nMaria')


@is_authorized
def app_version():
    print('v1.0')

@append_details
def user_data():
    return 'name: Mathias'


list_users()
app_version()
print(user_data())

