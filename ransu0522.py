# -*- coding: utf-8 -*-
import random
x = list(range(1,38))
w = [2, 2, 3, 7, 4, 2, 3, 6, 5, 6, 6, 1, 9, 8, 3, 5, 4, 5, 5, 7, 2, 6, 5, 5, 3, 5, 4, 1, 3, 6, 3, 2, 7, 6, 5, 3, 2 ]
s = random.choices(x, k = 10000, weights = w)

for i in x:
  print(i, ':', s.count(i))
