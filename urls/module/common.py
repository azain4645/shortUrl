import math

class ShortURL(object):

    def __init__(self):
        self.baseString = "123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNOPRSTUVWXYZ"
        self.baseLength = len(self.baseString)

    def encode(self, num):
        #return format(num, 'x')
        if not int(num):
            raise ValueError('must be integer')
            pass

        encode = ''

        while num:
            remainder = (num % self.baseLength)
            num = math.floor(num / self.baseLength)
            encode += self.baseString[remainder]
            pass

        return encode[::-1]
        pass

    def decode(self, key):
        #return int(code, base=16)
        if not str(key):
            raise ValueError('must be String')
            pass

        decode = 0

        while key:
            position = self.baseString.index(key[0])

            if position < 0:
                raise ValueError("'decode' can not find in the baseString")
                pass

            powerOf = len(key) - 1
            decode += position * math.pow(self.baseLength, powerOf)
            key = key[1::1]

            pass

        return int(decode)