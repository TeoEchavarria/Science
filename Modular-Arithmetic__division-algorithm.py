
def modularExpresionSolutions(strParam):
  strParam.strip()
  a = int(strParam[:strParam.find("x")])
  b = int(strParam[strParam.find("=")+1: strParam.find("(")].strip())
  c = int(strParam[strParam.find("d")+1: strParam.find(")")].strip())

  all = 0
  for i in range(c):
    if a % b == i or a*(i+1) % b in range(c):
      all+= 1

  return all


def euclides(num_1,num_2,iteration=1):
    if num_1<num_2:
        num_1,num_2=num_2,num_1

    rest  =num_1%num_2
    print(f'{num_1} = {num_2} * {int((num_1 - rest)/num_2)} + {rest}')
    if rest==0:
        return (num_2,iteration)

    return euclides(num_2,rest,iteration+1)

num_1=int(input('Numero 1° = '))
num_2=int(input('Numero 2° = '))

common_Divisor,iteration=euclides(num_1,num_2)

print(f'''
MCD ( {num_1} , {num_2} ) = {common_Divisor}''')

if __name__ == "__main__":
  n = "12x = 5 (mod 2)"
  b = "12x = 4 (mod 2)"
  c = "32x = 8 (mod 4)"
  print(MathChallenge(n))
  print(MathChallenge(b))
  print(MathChallenge(c))
