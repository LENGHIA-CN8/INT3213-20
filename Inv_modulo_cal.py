def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, b):
    g, x, y = egcd(a, b)
    if g != 1:
        print('Nghịch đảo Modulo không tồn tại')
    else:
        return x % b

a=int(input('Nhập số a'))
b=int(input('Nhập số b'))
print(modinv(a,b))