import sys

def parse(m):
    inc = 1
    str = ""
    list = []
    for i in range(len(m)):
        str = str + m[i]
        if inc >= 32:
            list.append(str)
            str = ""
            inc = 0
        inc = inc + 1
    return list


parse(sys.argv[1])

def mac(list):
    x0 = []
    y = []
    for i in range(256):
        x0[i] = 0
    y[1] = list[0]

#['49206C696B652066656564696E67206F', '6C6420736F636B7320746F2063617473', '2C20616E64204D696E67797565206973', '20746865206265737420636F776F726B']
#[1e9094630da6fa9f667f8fb8ead97064, e2397e27f0381cc002c566a970bc25fd, 1f8e6a2d1e42ab323f4c47cb3bfbba21

#y[2] = m[2] xor x[1] = 72f4b41062c591ec460be09889b80417
#y[3] = m[3] xor x[2] = ce191f49941851a96ca21fdc159c4c8e
#y[4] = m[4] xor x[3] = 3ffa02483e20ce414b6c24a44c94c84a

#mac is bfd00607e3bf371d07bf5e5309dd6e88
