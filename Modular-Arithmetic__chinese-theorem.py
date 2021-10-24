#---- BASIC FUNCTIONS -----

def multiply(lst):
    solution = 1
    for i in lst:
        solution *= i
    return solution

def Inverse(Cd_n,mod):
    rango = list(range(mod))
    rango.reverse()
    for i in rango:
        a = ((Cd_n*i)-1)/ mod
        b = ((Cd_n*i)-1)// mod
        if a == b :
            return i


#----- CHINESE REMAINDER THEOREM -----

def chinese_theorem(residuo, module,n):
    product = multiply(module)
    Cd_n = [int(product/i) for i in module]
    Dd_n = [ Inverse(Cd_n[i], module[i]) for i in range(n)]
    pre_end = [ residues[i] * Cd_n[i] * Dd_n[i] for i in range(n)]
    end = sum(pre_end)
    
    return print(f'{end % product} + {product}t')





if __name__ == '__main__':

    #----- INPUT EQUATIONS -----
    n = int(input('Number of equations: '))
    residues = []
    modules = []
    for i in range(n):
        print(f' x = a_{i+1} mod b_{i+1}')
        residue_x = int(input(f'a_{i+1} = residue : '))
        module_x = int(input(f'b_{i+1}° = module  : '))
        print(f'\n x = {residue_x} mod {module_x} \n')
        residues.append(residue_x)
        modules.append(module_x)
    
    chinese_theorem(residues, modules, n)