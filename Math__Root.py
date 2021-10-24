#---EXHAUSTIVO-----

def while_exhastive(solution, index,  radicand, e):
    while solution**index < radicand:
        solution +=10**-e
    return solution

def exhastive(index, radicand):
    solution = 0
    solution = while_exhastive(solution, index, radicand, 0)
    
    if solution**index == radicand:
        return solution
    elif solution**index < radicand:
        solution = while_exhastive(solution, index, radicand, 1)
        if solution**index == radicand:
            return solution
        elif solution**index < radicand:
            solution = while_exhastive(solution, index, radicand, 2)
            if solution**index == radicand:
                return solution
            elif solution**index < radicand:
                solution = while_exhastive(solution, index, radicand, 3)
                if solution**index == radicand:
                    return solution
                elif solution**index < radicand:
                    solution = while_exhastive(solution, index, radicand, 4)
                    return solution
                elif solution**index > radicand:
                    solution -= 0.0001
                    return solution
            
            elif solution**index > radicand:
                solution -= 0.001
                solution = while_exhastive(solution, index, radicand, 3)
                if solution**index == radicand:
                    return solution
                elif solution**index < radicand:
                    solution = while_exhastive(solution, index, radicand, 4)
                    return solution
                elif solution**index > radicand:
                    solution -= 0.0001
                    return solution
        elif solution**index > radicand:
            solution -= 0.1
            solution = while_exhastive(solution, index, radicand, 2)
            if solution**index == radicand:
                return solution
            elif solution**index < radicand:
                solution = while_exhastive(solution, index, radicand, 3)
                if solution**index == radicand:
                    return solution
                elif solution**index < radicand:
                    solution = while_exhastive(solution, index, radicand, 4)
                    return solution
                elif solution**index > radicand:
                    solution -= 0.0001
                    return solution
            
            elif solution**index > radicand:
                solution -= 0.01
                solution = while_exhastive(solution, index, radicand, 3)
                if solution**index == radicand:
                    return solution
                elif solution**index < radicand:
                    solution = while_exhastive(solution, index, radicand, 4)
                    return solution
                elif solution**index > radicand:
                    solution -= 0.001
                    solution = while_exhastive(solution, index, radicand, 5)
                    return solution
    
    elif solution**index > radicand:
        solution -= 1
        solution = while_exhastive(solution, index, radicand, 1)
        if solution**index == radicand:
            return solution
        elif solution**index < radicand:
            solution = while_exhastive(solution, index, radicand, 2)
            if solution**index == radicand:
                return solution
            elif solution**index < radicand:
                solution = while_exhastive(solution, index, radicand, 3)
                if solution**index == radicand:
                    return solution
                elif solution**index < radicand:
                    solution = while_exhastive(solution, index, radicand, 4)
                    return solution
                elif solution**index > radicand:
                    solution -= 0.0001
                    return solution
            
            elif solution**index > radicand:
                solution -= 0.001
                solution = while_exhastive(solution, index, radicand, 3)
                if solution**index == radicand:
                    return solution
                elif solution**index < radicand:
                    solution = while_exhastive(solution, index, radicand, 4)
                    return solution
                elif solution**index > radicand:
                    solution -= 0.0001
                    return solution
        elif solution**index > radicand:
            solution -= 0.1
            solution = while_exhastive(solution, index, radicand, 2)
            if solution**index == radicand:
                return solution
            elif solution**index < radicand:
                solution = while_exhastive(solution, index, radicand, 3)
                if solution**index == radicand:
                    return solution
                elif solution**index < radicand:
                    solution = while_exhastive(solution, index, radicand, 4)
                    return solution
                elif solution**index > radicand:
                    solution -= 0.0001
                    return solution
            
            elif solution**index > radicand:
                solution -= 0.01
                solution = while_exhastive(solution, index, radicand, 3)
                if solution**index == radicand:
                    return solution
                elif solution**index < radicand:
                    solution = while_exhastive(solution, index, radicand, 4)
                    return solution
                elif solution**index > radicand:
                    solution -= 0.001
                    solution = while_exhastive(solution, index, radicand, 5)
                    return solution


#----- Bisection -----
def bisection(index, radicand):
    epsilon= 0.0001
    solution = 0
    under = 0
    high = radicand
    while abs(solution**index - radicand) >= epsilon :
        if solution**index < radicand:
            under = solution
        else:
            high = solution

        solution = (high+under)/2
    return solution


#----- Newton Raphson -----



def f(x,index, radicand):
    return (x**index) - radicand
def f_prima(x, index):
    return index*(x**(index-1))

def Newton_Raphson(index, radicand):
    epsilon = 0.0001
    x_initial= 0
    tramo = 0.01
    if x_initial == radicand:
        return 0
    else:
        x_initial = 1

    while not(tramo <= epsilon):
        x_new = x_initial - (f(x_initial,index, radicand)/f_prima(x_initial, index))
        tramo = abs(x_new-x_initial)
        x_initial = x_new
    return x_new



if __name__ == '__main__':
    n = float(input('Radicand = '))
    a = float(input('Index = '))

    print(f'''
    Exhaustive = {exhastive(a, n)}
    Bisection  = {bisection(a,n)}
    Newton Raphson = {Newton_Raphson(a,n)}
    ''')  

