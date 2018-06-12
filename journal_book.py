import os


def load(name):
    """
    This is the file IO
    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with file data
    """

    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())


def save(name, journal_data):
    filename = get_full_pathname(name)
    print("...... saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals' + name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)
