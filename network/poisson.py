import math
import random

POISSON_MIN = 0
POISSON_MAX = 100

class Poisson(object):
    def __init__(self):
        pass

    def poisson_function(self, lamb, x):
        if x >= POISSON_MAX:
            return 0

        denom = math.factorial(x)
        num = math.exp(-lamb) * (lamb**x)
        return num / denom

    def make_distribution(self, lamb):
        self.distribution = []
        prev = 0
        for x in range(POISSON_MAX):
            self.distribution.append((
                    x,
                    prev+self.poisson_function(lamb, x)
                    ))
            prev = self.distribution[x][1]

    def get_element(self, prob):
        buff = self.distribution[0]
        for x in self.distribution:
            if prob > x[1]:
                buff = self.distribution[x[0]+1]
            else:
                break
        return buff[0]

    def generate(self):
        prob = random.randint(0, 100)
        prob = float(prob)/100
        return self.get_element(prob)

if __name__ == '__main__':
    dist = poisson_dist(5)
    print get_element(dist, 0.99)
