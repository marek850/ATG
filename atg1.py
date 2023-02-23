def zoradPole(pole):
    for i in range(0, len(pole)):    
        for j in range(i+1, len(pole)):    
            if(pole[i] < pole[j]):    
                temp = pole[i]   
                pole[i] = pole[j] 
                pole[j] = temp

def jeDobre(pole):
    jeDobre = False
    for i in range(len(pole)):
        if i == 0:
            if pole[i] == 1:
                for j in range(1, len(pole)):
                    jeDobre = True
                    if pole[j] != 0:
                        jeDobre = False
    return jeDobre

def jeZle(pole):
    jeZle = False
    for i in range(len(pole)):
        if pole[i] < 0:
            jeZle = True
    return jeZle

def main():
    pocetVrcholov = int(input("Zadaj pocet vrcholov: "))
    stupneVrcholov = []
    for i in range(pocetVrcholov):
        pocet = i + 1
        stupneVrcholov.append(int(input(f"Zadaj {pocet}. stupen  vrchola: ")))
    zoradPole(stupneVrcholov)
    print(stupneVrcholov)
    for j in range(len(stupneVrcholov)):
       
        temp = stupneVrcholov[j]
        for k in range(1,temp+1):
            stupneVrcholov[j] = 0
            stupneVrcholov[j+k] -= 1
        zoradPole(stupneVrcholov)
        if jeDobre(stupneVrcholov):
            print("Uspesny graf")
            break
        if  jeZle(stupneVrcholov):
            print("Neuspesny Graf")
            break
    
main()