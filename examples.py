import ascii_graphing as ag
import math

# Simple sin wave with default dimensions.
print('=== Example 1 ===')
c = ag.Canvas()
c.add_func(math.sin)
c.flush()



# Customizing dimensions.
print('=== Example 2 ===')
c = ag.Canvas(height=20, width=20, border=True)
c.add_func(lambda x: x + 1, draw_char='-')
c.add_func(lambda x: 2 * math.sin(x) - 1)
c.add_point(-5, 5, 'X')
c.flush()