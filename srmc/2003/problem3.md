Пусть $0 &lt; a &lt; b &lt; 1$ являются действительными числами и
$$
g(x)=
\begin{cases}
x+1-a, &amp; \text{если $0 &lt; x &lt; a$,}\\
b-a, &amp; \text{если $x=a$,}\\
x-a, &amp; \text{если $a &lt; x &lt; b$,}\\
1-a, &amp; \text{если $x=b$,}\\
x-a, &amp; \text{если $b &lt; x &lt; 1$.}
\end{cases}
$$
Положим, что для некоторого натурального числа $n$ найдутся $n + 1$ действительных чисел 
$0 &lt; x_0 &lt; x_1 &lt; \ldots &lt; x_n &lt; 1$ таких, что $g^n(x_i)=x_i$ для $0 \le i \le n$. 
Докажите, что существует натуральное число $N$ такое, что $g^N(x)=x$ для всех $0 &lt; x &lt; 1$. 
(Обозначение: $g^k(x) = \underbrace{g(g(\ldots(g}_{k \text{ раз}}(x))\ldots))$).