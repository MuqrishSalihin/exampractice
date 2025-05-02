#include <stdio.h>
#include <stdlib.h>
#include <math.h>



int main () {
    int arr[] = {1,2,3,4,6,7,9,8,10,-4,100,56,27,39,50,-89};
    int length = sizeof(arr) / sizeof(arr[0]);

    int *max_list = (int *)malloc(length*sizeof(int));
    int *min_list = (int *)malloc(length*sizeof(int));

    int max_val;
    int min_val;

    int max_count = 0;
    int min_count = 0;

    for (int i = 0; i<length; i+=2){
        if (arr[i] > arr[i+1]) {
            max_list[max_count++] = arr[i];
            min_list[min_count++] = arr[i+1];
        }else {
            max_list[max_count++] = arr[i+1];
            min_list[min_count++] = arr[i];
        }
    }
//finding the max value

    max_val = max_list[0];
    min_val = min_list[0];

    for (int i = 1; i < max_count; i++){
        if (max_list[i] > max_val) 
            max_val = max_list[i];

    }

    for (int i = 1; i < min_count; i++){
        if (min_list[i] < min_val)
            min_val = min_list[i];
    
    }

    printf("The maximum value of the array = %d\n", max_val);
    printf("The minimum value of the array = %d\n", min_val);

    free(max_list);
    free(min_list);
}