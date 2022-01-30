### Ex 3.12

$v_\pi(s) = E_\pi[G_t|S_t=s] = \sum_{a\in A}\pi(a|s)p(G_t|s)$

$q_\pi(s,a)=E_\pi[G_t|s,a] = \sum_{a\in A}\pi(a|s)p(G_t|s,a) \\ =  \sum_{a\in A}p(G_t,a|s) = p(G_t|s)$

Thus, $v_\pi(s) = \sum_{a\in A}\pi(a|s)p(G_t|s) \\= \sum_{a\in A}\pi(a|s)q_\pi(s,a)$

### Ex 3.13

