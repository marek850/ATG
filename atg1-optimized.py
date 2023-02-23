def zorad(array):
    return sorted(array, reverse=True)

def existujeGraf(array):
    if array[0] != 1:
        return False
    for i in range(1, len(array)):
        if array[i] != 0:
            return False
    return True

def maZaporneHodnoty(array):
    return any(x < 0 for x in array)

def main():
    num_vertices = int(input("Zadaj pocet vrcholov: "))
    degrees = []
    for i in range(num_vertices):
        degree_num = i + 1
        degrees.append(int(input(f"Zadaj {degree_num}. stupen  vrchola: ")))
    sorted_degrees = zorad(degrees)
    print(sorted_degrees)
    for j in range(len(sorted_degrees)):
        temp = sorted_degrees[j]
        for k in range(1, temp+1):
            sorted_degrees[j] = 0
            sorted_degrees[j+k] -= 1
        sorted_degrees = zorad(sorted_degrees)
        if existujeGraf(sorted_degrees):
            print("Uspesny graf")
            break
        if maZaporneHodnoty(sorted_degrees):
            print("Neuspesny Graf")
            break

main()
