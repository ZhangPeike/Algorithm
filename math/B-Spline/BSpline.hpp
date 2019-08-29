#include <eigen3/Eigen/Core>
#include <eigen3/Eigen/Eigen>
#include <iostream>
#include <vector>

namespace bspline_pk {
class BSpline {
private:
  /* data */
  int spline_order_;
  int num_knots_per_second_;
  std::vector<double> knots_;
  std::vector<Eigen::MatrixXd> basis_matrices_;
  Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic, Eigen::ColMajor>
    coeffcients_;

public:
  BSpline(int spline_order, int num_knots_per_sec)
    : spline_order_(spline_order), num_knots_per_second_(num_knots_per_sec) {}
  ~BSpline() {}
  void InitSpline(const Eigen::VectorXd &times,
                  const Eigen::MatrixXd &interpolation_points, int num_segments,
                  double lambda);
  int NumCoeffReq(const int num_time_seg) const {
    return num_time_seg + spline_order_ - 1;
  }
  int NumKnotsReq(const int num_time_seg) const {
    return NumCoeffReq(num_time_seg) + spline_order_;
  }
  Eigen::MatrixXd M(const int k, const int i);
  double d0(const int k, const int i, const int j) const {
    return (knots_[i] - knots_[j]) / (knots_[j + k - 1] - knots_[j]);
  }
  double d1(const int k, const int i, const int j) const {
    return (knots_[i + 1] - knots_[i]) / (knots_[j + k - 1] - knots_[j]);
  }
};
} // namespace bspline_pk