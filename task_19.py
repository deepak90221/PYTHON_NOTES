#Namedtuple - When and why should you use namedtuples?

from collections import namedtuple


Color = namedtuple('Color',['red', 'green', 'blue'])

color = Color(55,155,255)
print(color.red, color.green, color.blue)
                