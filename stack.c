#include <iostream>
#include <cstdlib>

using namespace std;

struct Stack {
    float* data;
    int top;
    int size;
};

void push(Stack* s, float value) {
    if (s->top == s->size - 1) {
        s->size *= 2;
        s->data = (float*)realloc(s->data, s->size * sizeof(float));
    }
    s->top++;
    s->data[s->top] = value;
}

int main() {
    Stack s;
    s.top = -1;
    s.size = 1;
    s.data = (float*)malloc(s.size * sizeof(float));

    push(&s, 3.14);
    push(&s, 2.71);

    cout << "Stack contents: ";
    for (int i = 0; i <= s.top; i++) {
        cout << s.data[i] << " ";
    }
    cout << endl;

    free(s.data);
    return 0;
}
