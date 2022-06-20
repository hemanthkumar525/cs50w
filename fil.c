#include<stdio.h>
#include<process.h>
int main()
{
    FILE *ft,*fs;
    int c=0;
        fs=fopen("a.txt","r");
        fs=fopen("b.txt","w");
        if(fs==NULL)
        {
            printf("source file error\n");
            exit(1);
        }
        else if(ft==NULL)
        {
            printf("target file openinng\n");
            exit(1);
        }while (!feof(fs))
        {
            fputc(fgetc(fs),ft);
            c++;
        }
        printf("%d bytes copied from a top b",c);
        c=fcloseall();
        printf("%d filee is closed");
        return 0;
        
}