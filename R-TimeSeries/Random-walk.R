x = NULL
x[1] = 0
for(i in 2:1000){
  x[i] = x[i-1] + rnorm(1);
}
caminata_aleatoria = ts(x)
plot(caminata_aleatoria)
acf(caminata_aleatoria)
plot(diff(caminata_aleatoria))
