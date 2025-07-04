#include <stdio.h>  
void main( )  
{  
    int x = -1, y = 1, z = 0;  
    if(x && y++ && z)  
    ++x, y++, --z;  
    printf("%d, %d, %d", x++, y++, z++);  
}  

