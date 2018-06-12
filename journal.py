import journal_book


def main():
    print_header()
    run_event_loop()


def print_header():
    print('------------------')
    print('  Journal APP ')
    print('------------------')


def run_event_loop():
    print('What do you want to do with your journal?')

    journal_data = []
    cmd = "empty"
    while cmd != 'x' and cmd :

        cmd = input('[L]ist entries, [A]dd entry, E[x]it: ')
        cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)

        elif cmd == 'a':
            add_entry(journal_data)

        elif cmd != 'x' and cmd:
            print('WTF, we don\'t understand')

        print('Done, goodbye.')


def list_entries(data):
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal_book.add_entry(text, data)


main()
