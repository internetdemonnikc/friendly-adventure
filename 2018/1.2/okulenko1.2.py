a = input()
input_val = a.split('!')
n = int(input_val[-1])
chislo = input_val[0]

c = int(chislo)
bin(c)
h = list(bin(c))[-n:]
clear_val = []
for item in range(len(h)):
    if item >= 1:
         clear_val.append('0')
    if item == 0:
        clear_val.append('0')
k = list(bin(c))[0:n - 1:]
lk = k + clear_val

ll = ''.join(lk)

op = int(ll, 2)

print(chislo)
print(list(bin(c)))
print(bin(c))
print(h)
print(clear_val)
print(k)
print(lk)

print(ll)
print(op)
