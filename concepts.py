from collections import namedtuple

server_tuple = namedtuple('Server', ['name','ip', 'status'])
master = server_tuple('Mainframe', '198.162.1.12', 'online')

print(master.name, '\n', master.ip, '\n', master.status)