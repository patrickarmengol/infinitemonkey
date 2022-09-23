import random

def monkey_keystroke():
    possible_chars = 'abcdefghijklmnopqrstuvwxyz '
    return random.choice(possible_chars)

def main():
    to_find = 'hello'
    window_size = len(to_find)
    buf = '~' * window_size # bogus init
    while True:
        new_char = monkey_keystroke()
        print(new_char, end='')
        buf = buf[1:] + new_char
        if buf == to_find:
            print('<--')
            break

if __name__ == '__main__':
    main()