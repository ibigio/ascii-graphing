from keyword import kwlist
import math, time
from operator import truediv

class Canvas:
    def __init__(self, height=50, width=50, min_x=None, max_x=10, min_y=None, max_y=10, border=False):
        if min_x is None:
            min_x = -max_x
        if min_y is None:
            min_y = -max_y

        self.border = border
        self.set_border('+')
        self.set_dimensions(height, width, min_x, max_x, min_y, max_y)
        self.clear()

    def set_dimensions(self, height=None, width=None, min_x=None, max_x=None, min_y=None, max_y=None):
        
        # TODO: implement input validation
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if min_x is not None:
            self.min_x = min_x
        if max_x is not None:
            self.max_x = max_x
        if min_y is not None:
            self.min_y = min_y
        if max_y is not None:
            self.max_y = max_y

    def clear(self):
        self.grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def __safe(self, f):
        def safe_f(x):
            try:
                return f(x)
            except:
                return None
        return safe_f

    
    def add_func(self, f, draw_char='O'):
        x_range = self.max_x - self.min_x
        x_delta = x_range / self.width
        
        x = self.min_x
        y = self.min_y

        safe_f = self.__safe(f)

        for j in range(self.width):
            x = self.min_x + (j * x_delta)
            y = safe_f(x)
            if y is None:
                continue
            i, _ = self.__xy_to_ij__(x,y)
            if 0 < i < len(self.grid):
                self.grid[i][j] = draw_char
    
    def set_border(self, draw_char='+'):
        self.border_char = draw_char

    def flush(self):
        final = ''
        border_line = self.border_char * (3 * len(self.grid[0]))
        if self.border:
            final += border_line + '\n'
        for row in self.grid:
            s = '  '.join(row)
            if self.border:
                s = self.border_char + s + self.border_char
            if len(set(s)) == 1:
                final += '\n'
            else:
                final += s + '\n'
        if self.border:
            final += border_line
        print(final)


    def add_point(self, x, y, draw_char='O'):
        i, j = self.__xy_to_ij__(x, y)
        if i >= len(self.grid) or i < 0:
            return
        if j >= len(self.grid[0]) or j < 0:
            return
        self.grid[i][j] = draw_char

    def __xy_to_ij__(self, x, y):
        x_range = self.max_x - self.min_x
        y_range = self.max_y - self.min_y
        x_percent_offset = (x - self.min_x) / x_range
        y_percent_offset = (y - self.min_y) / y_range
        j = x_percent_offset * self.width
        i = self.height - (y_percent_offset * self.height)
        return int(i), math.trunc(j)