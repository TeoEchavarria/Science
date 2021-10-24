
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
