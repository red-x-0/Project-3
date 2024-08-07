import shelve

def save_token(token, filename='token_shelve'):
    """
    Save the login token to a shelve database.

    :param token: The token to be saved.
    :param filename: The filename for the shelve database.
    """
    with shelve.open(filename, writeback=True) as db:
        db['token'] = token

def load_token(filename='token_shelve'):
    """
    Load the login token from a shelve database.

    :param filename: The filename for the shelve database.
    :return: The saved token or None if no token is found.
    """
    with shelve.open(filename) as db:
        return db.get('token')
