import random
import threading
import matplotlib.pyplot as plt

class Monkey:
    def __init__(self, name):
        self.name = name
        self.key_count = 0

    def keystroke(self):
        possible_chars = 'abcdefghijklmnopqrstuvwxyz '
        return random.choice(possible_chars)
    
    def type_until(self, desired):
        buf = '~' * len(desired)
        while True:
            new_char = self.keystroke()
            self.key_count += 1
            buf = buf[1:] + new_char
            if buf == desired:
                print(f'monkey {self.name} typed {desired} after {self.key_count} keystrokes')
                return self.key_count

def main():
    to_find = 'hello'

    monkey_names = ['dave', 'john', 'steve', 'scott', 'jim', 'veronica', 'samantha', 'kate', 'hannah', 'leah']
    monkeys = [Monkey(name) for name in monkey_names]
    threads = [threading.Thread(target=m.type_until, args = (to_find,)) for m in monkeys]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    xs = [m.name for m in monkeys]
    ys = [m.key_count for m in monkeys]

    plt.bar(xs, ys)
    plt.title("monkey stats")
    plt.show()
    
    

if __name__ == '__main__':
    main()