from util import problem

w = [0.2,0.3,0.9]
p = [25,3.4,3.3]
a = [1,1,1]
a0 = 2

c = [w[i]*p[i] for i in range(3)]

p = problem(w,c,a,a0)

print(p.solve_opt(debug=True))

print(p.solve_profit())

