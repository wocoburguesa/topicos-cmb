import math

POISSON_MIN = 0
POISSON_MAX = 100

def poisson_function(l, x):
    if x >= POISSON_MAX:
        return 0
    
    denom = math.factorial(x)
    num = math.exp(-l) * (l**x)
    return num / denom

def poisson_dist(l):
    intervals = []
    prev = 0
    for x in range(POISSON_MAX):
        intervals.append((
                x,
                prev+poisson_function(l, x)
                ))
        prev = intervals[x][1]

    return intervals

def get_element(distribution, prob):
    buff = distribution[0]
    for x in distribution:
        if prob > x[1]:
            buff = distribution[x[0]+1]
        else:
            break
    return buff[0]

if __name__ == '__main__':
    dist = poisson_dist(5)
    print get_element(dist, 0.99)
