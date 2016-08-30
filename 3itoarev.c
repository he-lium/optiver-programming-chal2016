#include <stdlib.h>
#include <stdio.h>

char * myItoaReversed(int number) {
   int cCount = 0;
   int num = number;
   int digit;
   char *result = malloc(sizeof(char) * 10);
   if (number == 0) {
      result[cCount++] = '0';
   } else {
      if (number < 0) {
         num *= -1;
         result[cCount++] = '-';
      }
      while (num > 0) {
         digit = num % 10;
         result[cCount++] = (char) (digit + '0');
         num /= 10;
      }
   }
   result[cCount] = '\0';
   return result;
}

int main() {
   int number;
   scanf("%d", &number);
   char * numberAsString = myItoaReversed(number);
   printf("%s\n", numberAsString);
}
