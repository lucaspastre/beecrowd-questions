t = int(input())
s = t % 60
m = t // 60 % 60
h = t // 3600 % 60
print('%d:%d:%d' % (h, m, s))
