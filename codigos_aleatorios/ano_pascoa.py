import sys

ano = int(sys.argv[1])

a = ano % 19
b = ano // 100
c = ano % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = (19 * a + b - d - g + 15) % 30
i = c // 4
k = c % 4
L = (32 + 2 * e + 2 * i - h - k) % 7
m = (a + 11 * h + 22 * L) // 451
mes = (h + L - 7 * m + 114) // 31
dia = 1+ (h + L - 7 * m + 114) % 31

print(f"A páscoa será {dia}/{mes}/{ano}")