#include <stdio.h>

int fuel(int i){
    int ii = i/3 - 2;
    if(ii <= 0) return 0;
    return ii + fuel(ii); 
}

int main(int argc, char *argv[])
{
    int total, entry;
    total = 0;
    while(scanf("%d", &entry) == 1) total += fuel(entry);
    printf("%d\n", total);
    return 0;
}
