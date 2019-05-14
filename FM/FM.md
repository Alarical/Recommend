
## FM系列算法原理

#### 1.FM背景

FM (Factorization Machine) 主要是为了解决数据稀疏的情况下，特征怎样组合的问题。目前主要应用于CTR预估以及推荐系统中的概率计算。下图是一个广告分类的问题，根据用户和广告位相关的特征，预测用户是否点击了广告。图片来源，详见参考1。

![image-20190506171131606](/Users/alaric/Library/Application Support/typora-user-images/image-20190506171131606.png)

$$
y=w_0+\sum_{i=1}^{n}w_i*x_i+\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}w_{ij}*x_i*x_j	\quad \text{(1)}
$$

$$y=w_0+\sum_{i=1}^{n}w_i*x_i+\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}w_{ij}*x_i*x_j$$

$$
W=
        \begin{pmatrix}
        \omega_{11} & \omega_{12}& ... &\omega_{1n} \\
        \omega_{21} & \omega_{22}& ... &\omega_{2n} \\
        \vdots &\vdots &\ddots &\vdots\\
       \omega_{n1} & \omega_{n2}& ... &\omega_{nn} \\
        \end{pmatrix}_{n\times n}
$$




```Math
SSE=\sum_{i=1}^{k}\sum_{p\subset C_i}|p-m_i|^2
```



#### 2.dafsdf

######  2.1adsf

$$
xxxxxxxxxx y=w_0+\sum_{i=1}^{n}w_i*x_i+\sum_{i=1}^{n-1}\sum_{j=i+1}^{n}w_{ij}*x_i*x_j  \quad \text{(1)}
$$


​				



#### 5.参考资料

[http://www.cs.cmu.edu/~wcohen/10-605/2015-guest-lecture/FM.pdf](http://www.cs.cmu.edu/~wcohen/10-605/2015-guest-lecture/FM.pdf)