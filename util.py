# Complexity Problem
# Input: w,c,[alpha_1,alpha_2,...,alpha_n],alpha_0
# Object: sum(w)*z^alpha_i
# st: c_iz^alpha_i+z^alpha_0 = 1

from math import pow,sqrt
from copy import copy
from scipy.optimize import root_scalar


class problem:
    def __init__(self, w, c, alpha, a_0) -> None:
        self.w = w[:]
        self.c = c[:]
        self.alpha = alpha[:]
        self.a0 = a_0
        self.dim = len(w)  # number of decision variables
        self.x = [-1]*self.dim  # set the inital value to be -1
        self.z = -1
        self.opt = -1
    
    # Constraint equals to 1
    def __const__(self,x:list[int]=None):
        if not x: x=self.x
        def f(z):
            # print(z,self.alpha)
            val = sum([self.w[i]*(pow(z,self.alpha[i])) for i in range(self.dim) if x[i]])\
                + pow(z,self.a0)\
                - 1
            return val
        return root_scalar(f,bracket=[0,1],method='bisect').root

    # @property
    def obj(self,x:list[int]=None,z = None):
        if not x: x=self.x
        if not z: z=self.z

        return sum([self.c[i]*(pow(z,self.alpha[i])) for i in range(self.dim) if x[i]])

    
    def solve(self,x):
        z = self.__const__(x)
        
        return self.obj(x,z)

    # optimal solution
    def solve_opt(self,debug = False):
        for state in range(1,1<<self.dim):
            tmp = [1 if state>>i&1 else 0 for i in range(self.dim)]
            tmp_obj = self.solve(tmp)
            if debug: print(tmp,tmp_obj)
            if self.opt<tmp_obj:
                self.x = tmp[:]
                self.opt = tmp_obj
        self.z = self.__const__(self.x)
        return self.opt,self.x

    # TO-do: opt1 : sort by decreasing order of (c_i/w_i), add into solution if  obj increase ...
    def solve_profit(self):
        tmp = [0]*self.dim
        r = [(self.c[i]/self.w[i], i) for i in range(self.dim)]
        r.sort(reverse=True)
        tmp_res = -1
        tmp_l = [0]*self.dim
        for _, idx in r:
            tmp[idx] = 1
            tmp_obj = self.solve(tmp)
            if tmp_res<tmp_obj:
                tmp_l = tmp[:]
                tmp_res = tmp_obj
        return tmp_res, tmp_l



'''
from numpy import exp,array
p_vector = array([29.7305015793236,18.6910154086921,14.7901572832209,14.2969948576425,8.86903229358341])
a_vector = array([-2.99081654575819,-2.56593447543393,-2.02301853582614,1.41484645298317,-1.16095493300663])

w = exp(a_vector/3)
c = w*p_vector
tor = 3

test = problem(w,c,tor)
test.opt()
test.opt1()
'''
