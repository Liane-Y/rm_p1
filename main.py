from util import problem
from multiprocessing import Pool, cpu_count
from numpy.random import randint, rand, seed

total = 1000
dim = 10

def check_porc(randomseed=None):
    if randomseed:
        seed(randomseed)
    # print(randomseed)
    w = [randint(1, 100) if i%2 else randint(1, 100)/100 for i in range(dim)]
    p = [randint(1,500)/10 for _ in range(dim)]
    p.sort(reverse=True)
    a = [randint(1, 10) if i%2 else randint(1, 10)/10 for i in range(dim)]
    a0 = 5

    c = [w[i]*p[i] for i in range(dim)]

    p = problem(w,c,a,a0)

    opt = p.solve_opt()
    profit = p.solve_profit()
    ratio = profit[0]/opt[0]
    return ratio,randomseed


if __name__ == '__main__':
    processors = Pool(cpu_count())
    res = []
    for i in range(total):
        res.append(processors.apply_async(check_porc, args=(i,)))
        # res.append(check_porc(i))

    processors.close()
    processors.join()

    res = [r.get() for r in res]
    res.sort()
    print("Done")
    print(res[:10])
