"""
Little kid
"""


def wrapper(name, age):
    """
    wrapper function
    """
    if name == 'Alice':
        print('Hi, Alice.')
    elif age < 12:
        print('You are not Alice, kiddo.')
    else:
        print('You are neither Alice nor a little kid.')



if __name__ == "__main__":
    wrapper("a", 1)
