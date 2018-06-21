def main():
    print_header()
    game_loop()

def print_header():
    print('game is starting')


def game_loop():

    creatures = []

    hero = None

    while True:

        cmd = input("Do you attack")
        if cmd == 'a':
            print('attack')

        elif cmd == 'r':
            print('runaway')

        elif cmd == 'l':
            print('look around')