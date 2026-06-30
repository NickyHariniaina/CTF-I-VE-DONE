#include <stdio.h>
#include <string.h>

unsigned long hash_string(char *str) {
    unsigned long h = 0x1505;
    int i;

    for (i = 0; str[i] != '\0'; i++) {
        h = (unsigned char)str[i] + (h * 0x21);
    }

    return h;
}

int main() {
    char secret[] = "iUbh81!j*hn!";
    unsigned long hash_value = hash_string(secret);

    printf("Secret : %s\n", secret);
    printf("Hash   : %lu (0x%lx)\n", hash_value, hash_value);

    return 0;
}
