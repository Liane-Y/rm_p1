# How to use

## initialize a problem

```python
from util import problem

w = [0.2,0.3,0.9]
p = [25,3.4,3.3]
alpha = [1,1,1]
a0 = 2

c = [w[i]*p[i] for i in range(3)]

p = problem(w,c,alpha,a0)
```


![](https://latex.codecogs.com/svg.image?w_i&space;=&space;e^{\alpha_i\cdot&space;v_i})

![](https://latex.codecogs.com/svg.image?c_i&space;=&space;p_i\cdot&space;w_i&space;=&space;p_i\cdot&space;e^{\alpha_i\cdot&space;v_i})

## Solve this problem

```python
# optimal solution
p.solve_opt(debug=True)

# profit-nested solution
p.solve_profit()
```

### Example

- check.py: an example shows how to generate a problem instance and solve it.
- main.py: an example shows how to generate several problems with random parameters and find the smallest ratio.