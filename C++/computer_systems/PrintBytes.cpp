#include <stdio.h>
typedef unsigned char *uchar_ptr;
void PrintBytes(uchar_ptr start, int size) {
  for (size_t i = 0; i < size; i++) {
    /* code */
    printf("%.2x ", start[i]);
  }
  printf("\n");
}
template <typename T> void PrintVar(T x) {
  PrintBytes((uchar_ptr)&x, sizeof(T));
}
void PrintVar(void *x) { PrintBytes((uchar_ptr)&x, sizeof(void *)); }
void TestPrintBytes(int val) {
  int ival = val;
  float fval = (float)ival;
  double dval = (double)ival;
  int *pval = &ival;
  PrintVar<int>(ival);
  PrintVar<float>(fval);
  PrintVar<double>(dval);
  PrintVar<void *>(pval);
}
int main() {
  TestPrintBytes(100);
  return 0;
}