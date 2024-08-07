import shelve

def save_token(token):
    with shelve.open('token_shelf') as shelf:
        shelf['token'] = token

def load_token():
    with shelve.open('token_shelf') as shelf:
        return shelf.get('token')

def remove_token():
    with shelve.open('token_shelf') as shelf:
        if 'token' in shelf:
            del shelf['token']
