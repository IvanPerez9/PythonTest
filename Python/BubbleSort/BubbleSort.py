'''
Created on 19 ago. 2018

@author: ivan1
JAVA


   public static void sortSimple(int[] a) {
        for (int i = 0; i < a.length; i++) {
            boolean sorted = true; //flag to check if any swapping made
            for (int j = 1; j < a.length - i; j++) {
                if (a[j] < a[j - 1]) { 
                    int temp = a[j - 1];
                    a[j - 1] = a[j];
                    a[j] = temp;
                    sorted = false;
                }
            }
            if (sorted) break;
        }
    }
'''

#Recorre lista y les cambia de posicion hasta estar ordenados

def bubblesort_list (list):
    for i, num in enumerate(list):
        for j in range(0, len(list)-1):
            if (list[j]> list[j+1]):
                swap(list,j,j+1);

    return list;

def swap (list,one,two):
    aux = list[one];
    list[one]=list[two];
    list[two] = aux;