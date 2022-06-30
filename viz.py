import ascii_graphing as ag
import math, time

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

    c = ag.Canvas(max_y = 1.5, max_x = 1.5, height=300, width=300)

    def t(offset=0, b=0):
        return lambda x: (math.tan(offset + min_offset) * x) + b

    for i in range(lines):
        b = (2 * (db*i)) - 1
        c.add_func(t(i * d, b))

    c.flush()




def animate():
    c = ag.Canvas(max_y = 5, max_x = 10, height=50*3, width=100*3)
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

c = ag.Canvas(height=30, width=30, max_y=2, max_x=4)
# c.add_func(math.tan)
# c.add_func(lambda x: math.sin(x) + math.sin(2*x))
c.add_func(lambda x: (1/(1+(x**2))) )
c.flush()
