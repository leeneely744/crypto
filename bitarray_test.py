from bitarray import bitarray

a=bitarray('001001001')

# loop by 3
for i in range(0, len(a), 3):
    print(a[i:i+3].to01() + '-', end='')