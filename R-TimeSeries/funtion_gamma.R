thetas = c(1,0.5,0.5, 0, 0 , 0)

y = function(grados, k, theta){
  aux = 0
  uper = grados-k+1
  for(i in 1:uper){
    aux = aux + (theta[i]*theta[i+k])
  }
  aux
}

print(y(2,0,thetas))
print(y(2,2,thetas))
