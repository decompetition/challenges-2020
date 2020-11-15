#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct task{
    struct task *next;
    int pid;
    char *name;
};

int find_rootkit(struct task* t) {
    if (t == NULL)
        return -1;

    do{
        if(t->pid == 1337 && strcmp(t->name, "h4x0r") == 0)
            return 1;
    } while((t = t->next));

    return 0;
}

struct task *alloc_task(const char *name, int pid, struct task* next) {
    struct task *t = malloc(sizeof(struct task));
    t->name = malloc(strlen(name) + 1);
    strcpy(t->name, name);

    t->pid = pid;
    t->next = next;
    return t;
}

int main(int argc, char** argv) {
    int  pid;
    char name[64];
    struct task* head = NULL;

    while(scanf("%s %d", name, &pid) == 2) {
        head = alloc_task(name, pid, head);
    }

    int result = find_rootkit(head);
    printf("find_rootkit() = %d\n", result);
    return 0;
}
