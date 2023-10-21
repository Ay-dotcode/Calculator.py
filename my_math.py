from math import sin as s, cos as c, tan as t, sqrt as sq, radians

dec_pls = 10

sin = lambda x: round(s(radians(x)), dec_pls)
cos = lambda x: round(c(radians(x)), dec_pls)
tan = lambda x: round(t(radians(x)), dec_pls)
sqrt = lambda x: round(sq(x), dec_pls)
