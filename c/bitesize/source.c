#include <stdio.h>
#include <stdlib.h>
#include <string.h>


// Compile with: gcc -no-pie -fno-stack-protector binary.c
// To call the win function (256 byte stack frame + 8 byte saved EBP):
// ./a.out 283 `python -c 'print("A"*256 + "B"*8 + non_null_bytes_of_addr_of_win)'`

void win() {
    printf("How did you get here??\n");
    exit(42);
}

void sum(int argc, char** argv) {
    char buffer[247];
    unsigned char size;

    size = atoi(argv[1]);
    printf("SIZE: %d\n", size);
    if(size > 247) {
        printf("Too long!\n");
        return;
    }

    memset(buffer, 0, 247);
    memcpy(buffer, argv[2], atoi(argv[1]));
    printf("Got: %s\n", buffer);
}

int main(int argc, char** argv) {
    if(argc < 3) {
        return 0;
    }

    sum(argc, argv);
    return 0;
}
