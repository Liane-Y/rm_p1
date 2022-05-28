from util import problem
from multiprocessing import Pool, cpu_count
from numpy.random import randint, rand, seed

total = 100000
dim = 3

def check_porc(randomseed=None):
    if randomseed:
        seed(randomseed)
    # print(randomseed)
    w = [randint(1, 1000)/100  for i in range(dim)]
    p = [randint(1,5000)/100 for _ in range(dim)]
    # p0 = randint(1,500)/10
    # p1 = randint(1,500)/10
    p.sort(reverse=True)
    a = [randint(1, 100)/10 for i in range(dim)]
    a0 = randint(1,100)/10

    c = [w[i]*p[i] for i in range(dim)]

    p = problem(w,c,a,a0)

    opt_v,opt_s = p.solve_opt()
    if tuple(opt_s)==(1,0,1):
        v1 = p.solve([1,0,0])
        v2 = p.solve([1,1,0])
        rr = max(v1,v2)/opt_v
        # print(rr,opt_s,opt_v,v1)
        if rr<0.5:
            print(rr)
    return (1,randomseed) if tuple(opt_s)!=(1,0,1) else (rr,randomseed)

if __name__ == '__main__':
    processors = Pool(cpu_count())
    res = []
    for i in range(total):
        res.append(processors.apply_async(check_porc, args=(i,)))
        # res.append(check_porc(i))

    processors.close()
    processors.join()

    res = [r.get() for r in res]
    print(min(res))
