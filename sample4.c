#include <stdio.h>

void main( )
{
   int i, j, k;
   for(i = 0, j = 0, k = 0; i < 4, k < 8, j < 10; i++)
   {
      printf("%d %d %d", i, j, k);
      j = j + 2;
      k = k + 3;
   }
}