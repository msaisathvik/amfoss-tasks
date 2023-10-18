#include <stdio.h>
int main()
{
    int x;
    printf("Enter a number: ");
    scanf("%d",&x);
    for (int i=0;i<x+1;i++){
        int count = 0;
        for (int j=1;j<i+1;j++){
            if (i%j==0) count++;
        }
        if (count == 2) printf("%d ",i);
    }
    return 0;
}