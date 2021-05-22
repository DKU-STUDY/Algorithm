#include <stdio.h>
#define MAX 100000
 
int stack[MAX];
int top = -1;
 
void push(int data) {
    if (top >= MAX - 1) return;
    stack[++top] = data;
}
 
void pop() {
    if (top < 0) return;
    stack[top--] = 0;
}
 
int main() {
    int inputnum, data, sum = 0;
    scanf("%d", &inputnum);
 
    for(int i=0; i<inputnum; i++){
        scanf("%d", &data);
        if (data == 0) pop();
        else push(data);
    }
 
    for (int i = 0; i <= top; i++)
        sum += stack[i];
    printf("%d\n", sum);
    return 0;
}
