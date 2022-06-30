# ASCII Graphing Library

A tiny, dependency-free ASCII graphing library made to display arbitrary 2D functions in the terminal. I made this when I was bored on a plane without internet, which is pretty much why there's no dependnecies – I didn't remember how to use matplotlib.

## Examples

### Simple Sine Wave
```
import ascii_graphing as ag
import math

c = ag.Canvas()
c.add_func(math.sin)
c.flush()
```
```






















                                    O  O  O                                         O  O  O                                         O  O  O
O                                O           O  O                                O           O                                O  O           O
   O                          O                    O                          O                 O                          O                    O
      O                    O                          O                 O  O                       O                    O                          O
         O           O  O                                O           O                                O  O           O
            O  O  O                                         O  O  O                                         O  O  O























```
### Layering Custom Functions
```
import ascii_graphing as ag

c = ag.Canvas(height=20, width=20, border=True)
c.add_func(lambda x: x + 1, draw_char='-')
c.add_func(lambda x: 2 * math.sin(x) - 1)
c.add_point(-5, 5, 'X')
c.flush()
```

```
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                                                          +
+                                                      -   +
+                                                   -      +
+                                                -         +
+                                             -            +
+               X                          -               +
+                                       -                  +
+                                    -                     +
+                                 -                        +
+O              O  O           -  O  O              O  O   +
+            O              -           O                 O+
+   O                 O  -     O                 O         +
+      O  O           -  O  O              O  O            +
+                  -                                       +
+               -                                          +
+            -                                             +
+         -                                                +
+      -                                                   +
+   -                                                      +
+-                                                         +
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```