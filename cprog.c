# include <stdio.h>
# include <string.h>

main()
{
int i;
char *input;
char *output;

memset(output,0,50);
memset(input,0,50);
printf("Please enter your name:");
gets(output);
for (i=0;output[i]==' ';i++);
strncpy(input,output,i);
/* printf("\n%s",input);*/
printf("The output name as required is:%s,%s",input,output);
}


