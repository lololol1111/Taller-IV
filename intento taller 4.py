#!/usr/bin/env python
# coding: utf-8

# # Ejercicio II
# ## 1) Calcular $P(X_n=1|X_0=1)$ 
# Para calcular $P(X_n=1|X_0=1) = p_{11}^{(n)}$, buscamos los valores proprios $\lambda_1, \lambda_2, \lambda_3$: 
# 
# $$det(P-\lambda I) = 0$$
# 
# $$det\left(\begin{vmatrix}-\lambda & 1 & 0\\ 0 & \frac{2}{3}- \lambda & \frac{1}{3} \\p & 1-p & -\lambda\end{vmatrix}\right) =\lambda^2\left(\frac{2}{3} -\lambda \right ) +\frac{p}{3} + \frac{ \lambda}{3} (1-p)$$
# 
# 
# $$ = 2 \lambda^2 - 3 \lambda ^3 +p + \lambda +\lambda p$$
# $$ = 3 \lambda^3 - 2\lambda^2 + (p-1)\lambda-p = 0$$
# $$(\lambda-1)(3\lambda^2+\lambda+p)=0$$
# $\lambda_1 = 1$ 
# 
# $\lambda_{2,3} = \frac{-1 \pm \sqrt{1-12p}}{6}$
# 
# 

# ### Soluciones reales
# Si $p\leq\frac{1}{12}$ entonces los tres valores proprios seran numerous reales y $p_{11}^{(n)}$ puede escribirse de la siguiente forma:
# 
# 
# $$p_{11}^{(n)}=a \lambda_1^n+b \lambda_2^n+c \lambda_3^n$$ 
# para algunas costantes *a*, *b* y *c*.
# 
# 
# Los primeros valores de $p_{11}^{(n)}$ se pueden obtener de la siguiente manera:  
# 
# 
# 
# \begin{array}{c c}
# \begin{cases}
# 1 = p_{11}^{(0)} = a \lambda_1^0 + b \lambda_2^0 + c \lambda_3^0 \\
# 0 = p_{11}^{(1)} = a \lambda_1^1 + b \lambda_2^1 + c \lambda_3^1 \\
# 0 = p_{11}^{(2)} = a \lambda_1^2 + b \lambda_2^2 + c \lambda_3^2
# \end{cases}
# & \Leftrightarrow
# \begin{cases}
# 1 = a  + b  + c  \\
# 0 = a + b \lambda_2^1 + c \lambda_3^1 \\
# 0 = a + b \lambda_2^2 + c \lambda_3^2
# \end{cases}
# \end{array}
# 
# donde: $\lambda_{2} = \frac{-1 + \sqrt{1-12p}}{6}$ y $\lambda_{3} = \frac{-1 - \sqrt{1-12p}}{6}$
# 
# 
# Procedemos a calcular los valores de las costantes  *a*, *b* y *c* en Python resolvendo el sistema:

# In[1]:


import sympy as sp
p = sp.symbols('p', real=True, positive=True, less_than=1/12)
P = sp.Matrix([[0, 1, 0], [0, 2/3, 1/3], [p, 1-p, 0]])
lambda1 = 1
lambda2 = (-1+sp.sqrt(1-12*p))/6
lambda3 = (-1-sp.sqrt(1-12*p))/6


# En este framento de codigo definimos $0<p\le\frac{1}{12}$ y nuestra matriz de transicion P.

# In[2]:


a, b, c = sp.symbols('a b c')
eq1 = sp.Eq(a + b + c, 1)
eq2 = sp.Eq(a*lambda1+ b*lambda2 + c*lambda3, 0)
eq3 = sp.Eq(a*lambda1**2 + b*lambda2**2 + c*lambda3**2, 0)
sol = sp.solve((eq1, eq2, eq3), (a, b, c))


# Ahora definimos nuestro sistema y resolvemos

# In[3]:


print('a = ', list(sol.values())[0])


# In[4]:


print('b = ', list(sol.values())[1])


# In[5]:


print('c = ', list(sol.values())[2])


# Dado que *c* resulta ser una costante bastante larga, no la sostituimos y rescribimos nuestra ecuacion para $p_{11}^{(n)}$ como:  
# $$p_{11}^{(n)}=\frac{p}{p-4} +b \lambda_2^n+c \lambda_3^n$$ 
# para los valores calculados previamente de *b*, *c*, *$\lambda_2$* y *$\lambda_3$*

# ### Solucciones imaginarias
# Si $p>\frac{1}{12}$ tenemos que $\lambda_{2,3}=\frac{-1 \pm  i\sqrt{12p-1}}{6}$
# 
# y podemos escribir $p_{11}^n$ como:
# 
# $$ p_{11}^n = a+b\left( \frac{-1+ i\sqrt{12p-1}}{6}\right)^n + c\left( \frac{-1-i\sqrt{12p-1}}{6}\right)^n $$
# 
# Para expresar estos números complejos en términos de una potencia n, usamos la fórmula de Moivre, por la cual:
# 
# 
# $z^n = r^n  (cos(n\theta) + i  sin(n\theta))$
# 
# Donde: 
# - $r = [z] = \sqrt{a^2+b^2}$
# - $\theta= \tan ^ {-1} \left(\frac{b}{a}\right)$
# 
# 
# 
# En nuestro caso, para expresar $\lambda_{2} = \frac{-1 + \sqrt{1-12p}}{6}$ tenemos $a=-\frac{1}{6}$ y $ b=\frac{\sqrt{12p-1}}{6}$.
# 
# Y para expresar $\lambda_{3} = \frac{-1 - \sqrt{1-12p}}{6}$ tenemos $a=-\frac{1}{6}$ y $ b=-\frac{\sqrt{12p-1}}{6}$.
# 
# 
# 
# Entonces tendremos:
# 
# $r= \sqrt{\frac{1}{36} + \frac{12p-1}{36}} = \sqrt{\frac{1+12p-1}{36}} = \frac{\sqrt{12p}}{6} =\frac{\sqrt{3p}}{3}$
# 
# 
# $\theta_2= \tan^{-1} (-\sqrt{12p-1})$ y $\theta_3= \tan^{-1} (\sqrt{12p-1})$
# 
# 
# 
# Por lo tanto, llamando $\theta = tan^{-1}\sqrt{12p-1}$:
# 
# $$\lambda_2^n=\left( \frac{\sqrt{3p}}{3}\right)^n \left( \cos\theta-i\sin\theta\right)^n = \left( \frac{\sqrt{3p}}{3}\right)^n \left( \cos n\theta-i\sin n\theta\right)$$
# 
# 
# 
# $$\lambda_3^n=\left( \frac{\sqrt{3p}}{3}\right)^n \left( \cos\theta+i\sin\theta\right)^n = \left( \frac{\sqrt{3p}}{3}\right)^n \left( \cos n\theta+i\sin n\theta\right)$$
# 
# 
# 
# Consigue que:
# 
# $$ p_{11}^n = a+\left( \frac{\sqrt{3p}}{3}\right)^n\left( b \cos n\theta-bi\sin n\theta\right) + \left( \frac{\sqrt{3p}}{3}\right)^n \left( c \cos n\theta+ci\sin n\theta\right)$$
# 
# $$ = a+\left( \frac{\sqrt{3p}}{3}\right)^n\left( b \cos n\theta-bi\sin n\theta + c \cos n\theta+ci\sin n\theta\right)$$
# 
# $$ = \alpha +\left( \frac {\sqrt{3p}}{3}\right)^n\left[ \beta \cos n\theta + \gamma\sin n\theta\right]$$
# 
# 
# Donde $\beta=b+c$ y $\gamma=ci - bi$
# 
# 

# Substituyendo para los primeros valores de n tendriamos que:
# 
# \begin{array}{c c}
# \begin{cases}
# 1=p_{11}^{(0)} = \alpha + (\beta \cos0 + \gamma\sin0) = \alpha+ \beta \\
# 0=p_{11}^{(1)} = \alpha + \left( \frac{\sqrt{3p}}{3}\right) \left(\beta\cos \theta+\gamma\sin \theta\right) \\
# 0=p_{11}^{(2)} = \alpha + \left( \frac{\sqrt{3p}}{3}\right)^2 \left(\beta\cos 2\theta+\gamma\sin 2\theta\right)
# \end{cases}
# \end{array}
# 
# 

# Sabiendo que:
# $$\cos(\arctan(x))=\frac{1}{\sqrt{1+x^2}}$$ y 
# $$\sin(\arctan(x))=\frac{x}{\sqrt{1+x^2}}$$
# 
# 
# Tenemos que
# 
# 
# $$\cos(\theta) = \frac{1}{\sqrt{1 + (12p-1)}} = \frac{1}{\sqrt{12p}}$$ y
# 
# $$\sin(\theta) = \frac{\sqrt{12p-1}}{\sqrt{1 + 12p-1}} = \sqrt{\frac{12p-1}{12p}}$$.
# 
# 

# Para calcular $\cos(2\theta)$ y $\sin(2\theta)$ recordemos que:
# 
# $$\cos(2\theta) = \cos^2(\theta) - \sin^2(\theta)$$
# 
# $$\sin(2\theta) = 2\sin(\theta)\cos(\theta)$$ 
# 
# Entonces
# 
# 
# 
# $$\cos(2\theta) = \left(\frac{1}{\sqrt{12p}}\right)^2 - \left(\sqrt{\frac{12p-1}{12p}}\right)^2= \frac{2-12p}{12p}= \frac{1-6p}{6p}$$ y
# 
# 
# $$\sin(2\theta) = 2  \sqrt {\frac{12p-1}{12p}}\frac{1}{\sqrt{12p}} =  \frac{\sqrt{12p-1}}{6p}$$
# 

# Volviendo a las substituciones que hicimos antes: 
# 
# \begin{array}{c c c}
# \begin{cases}
# 1=p_{11}^{(0)} = \alpha + (\beta \cos0 + \gamma\sin0) = \alpha+ \beta \\
# 0=p_{11}^{(1)} = \alpha + \left( \frac{\sqrt{3p}}{3}\right) \left(\beta\cos \theta+\gamma\sin \theta\right) \\
# 0=p_{11}^{(2)} = \alpha + \left( \frac{\sqrt{3p}}{3}\right)^2 \left(\beta\cos 2\theta+\gamma\sin 2\theta\right)
# \end{cases}
# & \Leftrightarrow
# \begin{cases}
# 1 = \alpha+ \beta\\
# 0= \alpha + \left( \frac{\sqrt{3p}}{3}\right) \left(\beta\frac{1}{\sqrt{12p}}+\gamma\sqrt{\frac{12p-1}{12p}}\right)\\
# 0= \alpha +  \frac{3p}{9}\left(\beta\frac{1-6p}{6p}+\gamma\frac{\sqrt{12p-1}}{6p}\right)
# \end{cases}
# & \Leftrightarrow
# \begin{cases}
# 1= \alpha+ \beta \\
# 0= \alpha + \frac{1}{6}\left(\beta+\gamma\sqrt{12p-1}\right) \\
# 0=\alpha + \frac{1}{18}\left(\beta (1-6p)+\gamma\sqrt{12p-1}\right)
# \end{cases}
# \end{array}
# 
# 
# 

# In[6]:


pi = sp.symbols('p', real=True, positive=True, less_than=1, more_than=1/12)
alpha, beta, gamma = sp.symbols('alpha beta gamma')
eq1i = sp.Eq(alpha + beta , 1)
eq2i = sp.Eq(alpha + 1/6*( beta  + gamma * sp.sqrt(12*pi-1)), 0)
eq3i = sp.Eq(alpha +1/18*( beta * (1-6*pi) + gamma * sp.sqrt(12*pi-1)), 0)
sol_i = sp.solve((eq1i, eq2i, eq3i), (alpha, beta, gamma))


# In[7]:


print('alpha = ', list(sol_i.values())[0])


# In[8]:


print('beta = ', list(sol_i.values())[1])


# In[9]:


print('gamma = ', list(sol_i.values())[2])


# Entonces obtendriamos:  
# 
# 
# $$p_{1,1}^n = \frac{p}{p+2}+\left( \frac {\sqrt{3p}}{3}\right)^n\left[ \frac{2}{p+2} \cos n\theta + \gamma\sin n\theta\right]$$
# 
# 
# Donde $\gamma$ como anteriormente calculado. 

# ## 2) Encontrar la distribucion invariante
# Para encontrar la distribucion invariante escribimos: 
# 
# $$\pi P = (\pi_1,\pi_2,\pi_3)P = \left(p\pi_3, \pi_1 +\frac{2\pi_2}{3}+(1-p)\pi_3, \frac{\pi_2}{3}\right)= (\pi_1,\pi_2,\pi_3)$$
# 
# 

# \begin{array}{c c c}
# & \Leftrightarrow
# \begin{cases}
# p\pi_3= \pi_1 \\
# \pi_1 +\frac{2\pi_2}{3}+(1-p)\pi_3= \pi_2 \\
# \frac{\pi_2}{3}= \pi_3 \\
# \pi_1+ \pi_2 + \pi_3= 1 
# \end{cases}
# & \Leftrightarrow
# \begin{cases}
# \pi_1= p \pi_3 \\
# 3 p \pi_3 +2\pi_2+3 \pi_3 -3p\pi_3= 3\pi_2 \\
# \pi_2= 3 \pi_3 \\
# p \pi_2+ 3 \pi_3 + \pi_3= 1 
# \end{cases}
# & \Leftrightarrow
# \begin{cases}
# \pi_1= p \pi_3 \\
# 3 p \pi_3 +6 \pi_3+3 \pi_3 -3p\pi_3= 9 \pi_3 \\
# \pi_2= 3 \pi_3 \\
# \pi_3= \frac{1}{p+4} 
# \end{cases}
# \end{array}
# 
# \begin{array}{c c c}
# & \Leftrightarrow
# \begin{cases}
# \pi_1= \frac{p}{p+4} \\
# \pi_2= \frac{3}{p+4}  \\
# \pi_3= \frac{1}{p+4} 
# \end{cases}
# \end{array}
# 

# In[10]:


p = sp.symbols('p', real=True, positive=True, less_than=1)
pi1, pi2, pi3 = sp.symbols('pi1 pi2 pi3')
eq1 = sp.Eq(p*pi3-pi1, 0)
eq2 = sp.Eq(pi1 + 2/3*pi2-pi2+(1-p)*pi3, 0)
eq3 = sp.Eq(pi2/3-pi3, 0)
eq4 = sp.Eq(pi1+pi2+pi3, 1)
sol = sp.solve((eq1, eq2, eq3, eq4), (pi1, pi2, pi3))


# In[11]:


print(sol)


# Entonces la distribucion invariante es dada por: 
# $$\pi=\left(\frac{p}{p+4}, \frac{3}{p+4}, \frac{1}{p+4}\right) $$

# La probabilidad $P(X_n=1 | X_0=1)$ en estado estacionario se puede calcular de la siguiente manera:
# 
# $$P(X_n=1 | X_0=1) = \pi(1)$$ 
# 
# Tomando el limite por $n\rightarrow\infty$ de $P(X_n=1 | X_0=1)$ calculados en el punto *a*, obtenemos: 
# 
# - para las soliciones reales:
# 
# $$\lim_{n \to \infty} p_{11}^{(n)} = \lim_{n \to \infty}\frac{p}{p-4} +b \lambda_2^n+c \lambda_3^n = \frac{p}{p-4}=\pi(1)$$ 
# 
# Como esperado.
# 
# - para las soluciones imaginarias:
# 
# $$\lim_{n \to \infty} p_{11}^{(n)} = \lim_{n \to \infty} \frac{p}{p+2}+\left( \frac {\sqrt{3p}}{3}\right)^n\left[ \frac{2}{p+2} \cos n\theta + \gamma\sin n\theta\right] = \frac{p}{p+2}$$ 
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




