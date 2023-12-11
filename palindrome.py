#include <stdio.h>
#include <string.h>

int is_palindrome(char str[]) {
  int len = strlen(str);

  for (int i = 0, j = len - 1; i < j; i++, j--) {
    while (!isalnum(str[i])) {
      i++;
    }
    while (!isalnum(str[j])) {
      j--;
    }
    char ch1 = tolower(str[i]);
    char ch2 = tolower(str[j]);

    if (ch1 != ch2) {
      return 0;
    }
  }

  return 1;
}

int main() {
  char str[100];

  printf("Enter a string: ");
  fgets(str, 100, stdin);

  str[strcspn(str, "\n")] = '\0';

  if (is_palindrome(str)) {
    printf("%s is a palindrome.\n", str);
  } else {
    printf("%s is not a palindrome.\n", str);
  }

  return 0;
}
