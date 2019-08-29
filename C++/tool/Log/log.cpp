#include "log.hpp"
#include <mutex>
#include <sys/stat.h>
#include <unistd.h>
namespace zpk {
std::mutex pk_mutex;
std::string GetSrcFileName(const char *file_name_full_path) {
  char tmp[256] = {0};
  memcpy(tmp, file_name_full_path, strlen(file_name_full_path) + 1);
  std::string full_name = tmp;
  int pos_start = full_name.find_last_of("/");
  if (pos_start == -1) {
    pos_start = 0;
  }
  std::string file_name =
    full_name.substr(pos_start + 1, full_name.size() - pos_start);
  return file_name;
}
std::string GetCurrentSystemTime() {
  auto time_now = std::chrono::system_clock::now();
  auto tt = std::chrono::system_clock::to_time_t(time_now);
  auto duration_in_ms = std::chrono::duration_cast<std::chrono::milliseconds>(
    time_now.time_since_epoch());
  auto duration_in_s = std::chrono::duration_cast<std::chrono::seconds>(
    time_now.time_since_epoch());
  int theMs = duration_in_ms.count() - duration_in_s.count() * 1000;
  struct tm *ptm = localtime(&tt);
  char date[60] = {0};
  sprintf(date, "%d-%02d-%02d-%02d:%02d:%02d.%03d ", (int)ptm->tm_year + 1900,
          (int)ptm->tm_mon + 1, (int)ptm->tm_mday, (int)ptm->tm_hour,
          (int)ptm->tm_min, (int)ptm->tm_sec, theMs);
  return std::string(date);
}
long long GetCurrentMillisec() {
  auto time_now = std::chrono::system_clock::now();
  auto duration_in_ms = std::chrono::duration_cast<std::chrono::milliseconds>(
    time_now.time_since_epoch());
  return duration_in_ms.count();
}
void CurrentDateToString(std::string &time_str) {
  time_t rawtime;
  struct tm *timeinfo;
  char buffer[30];
  time(&rawtime);
  timeinfo = localtime(&rawtime);
  strftime(buffer, sizeof(buffer), "%Y_%m_%d_%H_%M_%S", timeinfo);
  time_str.clear();
  time_str = std::string(buffer);
  return;
}
FILE *fp;
std::string root_dir = "./log";
// TODO: make log like google glog, 1. set log path and prefix
int LogInit() {
  std::string current_date_time;
  CurrentDateToString(current_date_time);
  std::string log_path = root_dir + "/LOG_" + current_date_time;
  if (access(root_dir.c_str(), 00) != 0) {
    mkdir(root_dir.c_str(), S_IRWXU);
  }
  fp = fopen(log_path.c_str(), "a+");
  if (fp == NULL) {
    return -1;
  }
  fprintf(fp, "Log file created at: %s \n", current_date_time.c_str());
  fflush(fp);
  return 0;
}
int LogWrite(char *tmp) {
  if (fp) {
    pk_mutex.lock();
    fprintf(fp, "%s", tmp);
    fflush(fp);
    pk_mutex.unlock();
  }
  return 0;
}
int LogEnd() {
  if (fp) {
    fflush(fp);
    fclose(fp);
  }
  return 0;
}
} // namespace zpk