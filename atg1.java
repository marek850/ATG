import java.util.*;
public class Main {
    public static List<Integer> sortDescending(List<Integer> array) {
    Collections.sort(array, Collections.reverseOrder());
    return array;
}

public static boolean isGoodGraph(List<Integer> array) {
    if (array.get(0) != 1) {
        return false;
    }
    for (int i = 1; i < array.size(); i++) {
        if (array.get(i) != 0) {
            return false;
        }
    }
    return true;
}

public static boolean hasNegativeElements(List<Integer> array) {
    for (int x : array) {
        if (x < 0) {
            return true;
        }
    }
    return false;
}

public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.print("Zadaj pocet vrcholov: ");
    int numVertices = input.nextInt();
    List<Integer> degrees = new ArrayList<>();
    for (int i = 0; i < numVertices; i++) {
        int degreeNum = i + 1;
        System.out.printf("Zadaj %d. stupen vrchola: ", degreeNum);
        degrees.add(input.nextInt());
    }
    List<Integer> sortedDegrees = sortDescending(degrees);
    System.out.println(sortedDegrees);
    for (int j = 0; j < sortedDegrees.size(); j++) {
        int temp = sortedDegrees.get(j);
        for (int k = 1; k <= temp; k++) {
            sortedDegrees.set(j, 0);
            sortedDegrees.set(j+k, sortedDegrees.get(j+k) - 1);
        }
        sortedDegrees = sortDescending(sortedDegrees);
        if (isGoodGraph(sortedDegrees)) {
            System.out.println("Uspesny graf");
            break;
        }
        if (hasNegativeElements(sortedDegrees)) {
            System.out.println("Neuspesny graf");
            break;
        }
    }
}