#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

typedef struct {
    char data[MAX_SIZE];
    int top;
} Stack;

void initialize(Stack* stack) {
    stack->top = -1;
}

void push(Stack* stack, char ch) {
    if (stack->top == MAX_SIZE - 1) {
        printf("Stack Overflow\n");
        return;
    }
    stack->data[++stack->top] = ch;
}

char pop(Stack* stack) {
    if (stack->top == -1) {
        printf("Stack Underflow\n");
        return -1;
    }
    return stack->data[stack->top--];
}

char peek(Stack* stack) {
    if (stack->top == -1) {
        return -1;
    }
    return stack->data[stack->top];
}

int isBalanced(char* input) {
    Stack stack;
    initialize(&stack);
    
    for (int i = 0; input[i] != '\0'; i++) {
        char ch = input[i];
        
        if (ch == '{' || ch == '(' || ch == '[') {
            push(&stack, ch);
        } 
        else if (ch == '}' || ch == ')' || ch == ']') {
            if (stack.top == -1) {
                return 0; // Unmatched closing bracket
            }
            char topChar = pop(&stack);
            if ((ch == '}' && topChar != '{') ||
                (ch == ')' && topChar != '(') ||
                (ch == ']' && topChar != '[')) {
                return 0; // Mismatched brackets
            }
        }
    }
    
    return stack.top == -1; // Balanced if stack is empty
}

int main() {
    char input[MAX_SIZE];
    printf("Enter a string of brackets: ");
    scanf("%s", input);
    
    if (isBalanced(input)) {
        printf("The brackets are balanced.\n");
    } else {
        printf("The brackets are not balanced.\n");
    }
    
    return 0;
}
