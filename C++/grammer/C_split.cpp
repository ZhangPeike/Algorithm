#include <stdio.h>
#include <string.h>

int main() {
  // char str[] ="- This, a sample string.";
  char str[] = "./benchmark/MYNT_APRIL/static/cam0/1543912161435592890.png";
  char *pch;
  printf("Splitting string \"%s\" into tokens:\n", str);
  pch = strtok(str, "./");
  while (pch != NULL) {
    printf("%s\n", pch);
    pch = strtok(NULL, "./");
  }
  return 0;
}