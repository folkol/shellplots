import fileinput
from sys import stdout

xs = []
ys = []
for line in fileinput.input('points.dat'):
    x, y = line.split()
    xs.append(int(x))
    ys.append(int(y))

# Scale to sane size
# numpy array?

width = len(xs)
height = max(ys) - min(ys)
print max(ys), min(ys)

print('-' * (5 * width + 2))
for row in range(height):
    stdout.write('|')
    for i, e in enumerate(xs):
        stdout.write('  ')
        if row == ys[i]:
            stdout.write('*')
        else:
            stdout.write(' ')
        stdout.write('  ')
    print '|'
print('-' * (5 * width + 2))
