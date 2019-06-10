#include "BSpline.hpp"
#include <fstream>
typedef Eigen::Matrix<double, 6, 1> Vector6d;
int main() {
  std::cout << "Hello world. This is Bspline." << std::endl;
  bspline_pk::BSpline mybspline(6, 100);
  std::vector<Vector6d> poses;
  std::vector<double> times;
  std::ifstream ifs("./pose.txt");
  long int t0 = 0;
  Vector6d pose;
  ifs >> t0 >> pose[0] >> pose[1] >> pose[2] >> pose[3] >> pose[4] >> pose[5];
  times.push_back(0.0);
  poses.emplace_back(pose);
  long int t = 0;
  while (ifs >> t >> pose[0] >> pose[1] >> pose[2] >> pose[3] >> pose[4] >>
         pose[5]) {
    times.push_back((t - t0) / 1e6);
    poses.emplace_back(pose);
  }
  //   std::cout << "Poses:" << std::endl;
  //   for (size_t i = 0; i < poses.size(); i++) {
  //     std::cout << times[i] << " " << poses[i].transpose() << std::endl;
  //   }
  Eigen::Map<Eigen::VectorXd> etimes(times.data(), times.size());
  std::cout << "times: \n" << etimes;
  Eigen::MatrixXd eposes(6, poses.size());
  for (size_t i = 0; i < poses.size(); i++) {
    eposes.col(i) = poses[i];
  }
  //   std::cout << "Poses:\n" << eposes << std::endl;
  int num_knots_per_sec = 100;
  int num_segments =
    round(num_knots_per_sec * (times[times.size() - 1] - times[0]));
  mybspline.InitSpline(etimes, eposes, num_segments, 1e-4);
  return 0;
}