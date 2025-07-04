#include <stdio.h>  
#include <stdlib.h>  
void main( )  
{  
    int *ptr;  
    ptr = (int*) calloc(3, sizeof(int));  
    ptr[2] = 30;  
    printf("%d\n", *(ptr+2));  
    printf("%d", *ptr);  
    free(ptr);  
}  
