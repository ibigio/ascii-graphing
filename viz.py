import math, time

class Canvas:
    def __init__(self, height=50, width=50, min_x=None, max_x=50, min_y=None, max_y=50):
        self.height = height
        self.width = width
        if min_x is None:
            min_x = -max_x
        self.min_x = min_x
        self.max_x = max_x
        if min_y is None:
            min_y = -max_y
        self.min_y = min_y
        self.max_y = max_y

        self.clear()

    def clear(self):
        self.grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def add_axis(self):
        pass

    def safe(self, f):
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

        safe_f = self.safe(f)

        for j in range(self.width):
            x = self.min_x + (j * x_delta)
            y = safe_f(x)
            if y is None:
                continue
            i, _ = self.__xy_to_ij__(x,y)
            if 0 < i < len(self.grid):
                self.grid[i][j] = draw_char


    def flush(self):
        final = ''
        for row in self.grid:
            s = '  '.join(row)
            if len(set(s)) == 1:
                final += '\n'
            else:
                final += s + '\n'
                # print(s)
        print(final)


    def add_point(self, x, y):
        i, j = self.__xy_to_ij__(x, y)
        if i >= len(self.grid) or i < 0:
            return
        if j >= len(self.grid[0]) or j < 0:
            return
        self.grid[i][j] = True

    def __xy_to_ij__(self, x, y):
        x_range = self.max_x - self.min_x
        y_range = self.max_y - self.min_y
        x_percent_offset = (x - self.min_x) / x_range
        y_percent_offset = (y - self.min_y) / y_range
        j = x_percent_offset * self.width
        i = self.height - (y_percent_offset * self.height)
        return int(i), math.trunc(j)

def slices(lines=8):
    min_offset = -math.pi/4
    max_offset = math.pi/4
    d = (max_offset - min_offset) / (lines-1)
    db = 1/(lines)

    def intercept(m1,b1,m2,b2):
        '''
        Find x,y for interception of lines defined by
            y = m1x + b1
            y = m2x + b2
        '''
        x = (b2 - b1) / (m1 - m2)
        y = (m1 * x) + b1
        return x,y

    # Find x,y of intersection of outermost and second outermost lines.
    # m1 = math.tan(min_offset)
    # b1 = 0
    # max_x, max_y = intercept()

    c = Canvas(max_y = 1.5, max_x = 1.5, height=300, width=300)

    def t(offset=0, b=0):
        return lambda x: (math.tan(offset + min_offset) * x) + b

    for i in range(lines):
        b = (2 * (db*i)) - 1
        c.add_func(t(i * d, b))

    c.flush()




def animate():
    c = Canvas(max_y = 5, max_x = 10, height=50*3, width=100*3)
    p,q = 1,1

    def fpq(p=0, q=0):
        def f(x):
            y = (math.sin(x + p) + math.sin((x + q) * 2)) * (1/(1+((x/3)**2)))
            return y
        return f

    while True:
        c.add_func(fpq(p, q))
        c.flush()
        time.sleep(0.1)
        c.clear()
        p += 0.2
        q -= 0.05

animate()
# slices()

c = Canvas(height=30, width=30, max_y=2, max_x=4)
# c.add_func(math.tan)
# c.add_func(lambda x: math.sin(x) + math.sin(2*x))
c.add_func(lambda x: (1/(1+(x**2))) )
c.flush()
