data(co2)
help(co2)

plot(co2, main='Atmospheric CO2 Concentration')

co2_lineal_model = lm(co2 ~ time(co2))
co2_lineal_model$coefficients
help(lm)
abline(co2_lineal_model)

