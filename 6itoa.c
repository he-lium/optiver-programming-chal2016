#include <stdlib.h>
#include <stdio.h>

void swap(char v[], int i, int j) {
   int temp = v[i];
   v[i] = v[j];
   v[j] = temp;
}

void convertFromReverse(char *value, int lastIndex) {
   int i = (value[0] == '-') ? 1 : 0;
   while (i <= lastIndex) {
      swap(value, i, lastIndex+1);
      i++;
      lastIndex--;
   }
}

char * myItoa(int number) {
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
   result[cCount--] = '\0';
   convertFromReverse(result, cCount-1);
   return result;
}

int main() {
   int number;
   scanf("%d", &number);
   char * numberAsString = myItoa(number);
   printf("%s\n", numberAsString);
}
