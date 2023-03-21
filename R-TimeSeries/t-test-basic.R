X_1 = rnorm(100, mean= 100, sd= 30)
Y_1 = rnorm(100, mean= 95, sd= 30)

t.test(X_1,Y_1)
# Veamos como en este caso el p-value es mayor a 0.05 por lo que podriamos afirmar 
# que la hipotesis nula donde H_0 : mu = mu_0 es verdadera
# Lo que nos dice el p-valor es la probabilidad 

X_2 = rnorm(100, mean= 100, sd= 30)
Y_2 = rnorm(100, mean= 65, sd= 55)

t.test(X_2, Y_2)
# Como vemos aqui el p-value es mas pequeno que 0.05 entonces podemos afirmar 
# que la hipotesis alternativa es verdadera diciendo que ambas muestras son diferentes