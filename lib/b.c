#include<stdio.h>

int main () {
   FILE *fp;
   char str[] = "hi\n";

   fp = fopen( "./file.txt" , "w" );
   fwrite(str , 1 , sizeof(str) , fp );
   fclose(fp); 
   return(0);
}
