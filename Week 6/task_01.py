def DecimalToBinary(num):
    return bin(num).replace("0b","")

if __name__ == '__main__':
    print(DecimalToBinary(7))
    print(DecimalToBinary(32))