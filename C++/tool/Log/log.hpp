#ifndef __LOG_H__
#define __LOG_H__
#include <chrono>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
// #include <ratio>
#include <string>

namespace zpk {
// TODO: make it is used like glog.
const int size = 8192;
std::string GetSrcFileName(const char *file_name_full_path);
std::string GetCurrentSystemTime();
int LogInit();
int LogEnd();
int LogWrite(char *);
} // namespace zpk
// TODO: use <<
#define LOG(...)                                                                      \
  {                                                                                   \
    char tmp[8192] = {0};                                                             \
    sprintf(tmp, "[");                                                                \
    sprintf(tmp + 1, zpk::GetCurrentSystemTime().c_str());                            \
    sprintf(tmp + strlen(tmp), "%s %d] ", zpk::GetSrcFileName(__FILE__).c_str(),      \
            __LINE__);                                                                \
    sprintf(tmp + strlen(tmp), __VA_ARGS__);                                          \
    sprintf(tmp + strlen(tmp), "\n");                                                 \
    printf(tmp);                                                                      \
    zpk::LogWrite(tmp);                                                               \
  }
#endif