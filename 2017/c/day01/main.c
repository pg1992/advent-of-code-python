#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    char cur, prev, first;
    int accum = 0;

    scanf("%c", &first);
    prev = first;
    while (scanf("%c", &cur) != EOF) {
        if (cur == prev)
            accum += prev - '0';
        prev = cur;
    }

    if (cur == first)
        accum += cur - '0';

    printf("%i\n", accum);

    return EXIT_SUCCESS;
}
