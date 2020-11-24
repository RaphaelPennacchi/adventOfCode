#include <stdio.h>


int main(int argc, char *argv[])
{
    int total, entry;
    total = 0;
    while(scanf("%d", &entry) == 1) total += (entry/3 - 2);
    printf("%d\n", total);
    return 0;
}
