from phue import Bridge
from pprint import pprint as print

b = Bridge('192.168.1.202')

groups = b.groups
print(groups)

b.set_group('Alex Room', 'on', False)
