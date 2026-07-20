from stack import Stack

def valid(x, y, v):
    try:
        z = v[x][y]
        return True
    except IndexError:
        return False

