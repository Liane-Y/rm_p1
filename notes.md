# P1 Ratio

Problem P1:

$$
\max  \sum_{j\in S}P_jx_j(x_0)\\
s.t.  \sum_{j\in S}
x_j(x_0)+x_0=1
$$

Where $x_j(x_0)=e^{v_j \alpha_j}(x_0)^{\frac{\alpha_j}{\alpha_0}}$. 

There is an equivalence problem as following.

$$
\begin{align}
\max & \sum_{j\in S}p_j \beta_j z^{\alpha_j}\\
s.t. & \sum_{j\in S}\beta_j z^{\alpha_j}+z^{\alpha_0}=1\\
& \alpha_j\ge 1 ~~\forall j \in S\\
& \alpha_0\ge 1
\end{align}
$$


**Theorem 2** For assortment problems under the MEM, if there exists a product with the highest
profit, w.l.o.g. denoted as product 1, such that $\alpha_1$ ≥ $\alpha_0$  $\forall j\in Q$, then there exists a
strictly profit-nested set $S^*$ that is optimal.


- When $\alpha_0\le \underline{\alpha}$, profit nested solution is optimal
  
- When $\alpha_0\ge \underline{\alpha}\ge 1$:  
  Given any solution set $S$, consider the value of z.  
  - $\sum_{j\in S}\beta_j z^{\overline{\alpha}}+z^{\alpha_0}\le 1$   
  Which leads to the upper bound $z\le (\frac{1}{\sum_{j\in S}\beta_j})^{({1}/{\overline{\alpha}})}$
  - $z\le 1$
  - $\sum_{j\in S}\beta_j z^{\underline{\alpha}}+z^{\underline{\alpha}}\ge 1$   
  Which leads to the lower bound $z\ge (\frac{1}{\sum_{j\in S}\beta_j+1})^{({1}/{\underline{\alpha}})}$  

  Thus, $\underline{z}= (\frac{1}{\sum_{j\in S}\beta_j+1})^{({1}/{\underline{\alpha}})}$ and $\overline{z} = \min\{1,(\frac{1}{\sum_{j\in S}\beta_j})^{({1}/{\overline{\alpha}})}\}$
  - When $\sum\beta_j\le 1$:   
  $\underline{z}/\overline{z}\ge (\frac{1}{\sum_{j\in S}\beta_j+1})^{({1}/{\underline{\alpha}})}\ge\frac{1}{2}^{{({1}/{\underline{\alpha}})}}$
  - When $\sum\beta_j\ge 1$:   
  $\underline{z}/\overline{z} \ge\
  (\frac{1}{\sum_{j\in S}\beta_j+1})^{({1}/{\underline{\alpha}})}/(\frac{1}{\sum_{j\in S}\beta_j})^{({1}/{\overline{\alpha})}}
  $  
  When $\sum \beta\rarr \infin$, $(\frac{1}{\sum_{j\in S}\beta_j+1})^{({1}/{\underline{\alpha}})}/(\frac{1}{\sum_{j\in S}\beta_j})^{({1}/{\overline{\alpha})}} \rarr 0$  
  for example:
  $\underline{\alpha}=1,\overline{\alpha}=10$:  $\frac{x^{0.1}}{(x+1)} = 0$ when $x\rarr \infty$ 