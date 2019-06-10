#include "BSpline.hpp"
namespace bspline_pk {

Eigen::MatrixXd BSpline::M(const int k, const int i) {
  if (k == 1) {
    Eigen::MatrixXd M(1, 1);
    M(0, 0) = 1;
    return M;
  } else {
    Eigen::MatrixXd M_km1 = M(k - 1, i);
    Eigen::MatrixXd M1 = Eigen::MatrixXd::Zero(k, k - 1);
    Eigen::MatrixXd M2 = Eigen::MatrixXd::Zero(k, k - 1);
    M1.topRows(k - 1) = M_km1;
    M2.bottomRows(k - 1) = M_km1;
    Eigen::MatrixXd A = Eigen::MatrixXd::Zero(k - 1, k);
    for (int l = 0; l < k - 1; l++) {
      int j = i - k + 2 + l;
      A(l, l) = 1 - d0(k, i, j);
      A(l, l + 1) = d0(k, i, j);
    }
    Eigen::MatrixXd B = Eigen::MatrixXd::Zero(k - 1, k);
    for (int l = 0; l < k - 1; l++) {
      int j = i - k + 2 + l;
      B(l, l) -= d1(k, i, j);
      B(l, l + 1) = d1(k, i, j);
    }
    Eigen::MatrixXd M = M1 * A + M2 * B;
    return M;
  }
}
void BSpline::InitSpline(const Eigen::VectorXd &times,
                         const Eigen::MatrixXd &interpolation_points,
                         const int num_segments, const double lambda) {
  int num_knots = NumKnotsReq(num_segments);
  int num_coeff = NumCoeffReq(num_segments);
  int num_dimension = interpolation_points.rows();
  std::vector<double> knots(num_knots);
  double dt = (times[times.size() - 1] - times[0]) / num_segments;
  for (int i = 0; i < num_knots; i++) {
    knots[i] = times[0] + (i - spline_order_ + 1) * dt;
  }
  knots_ = knots;
  coeffcients_ = Eigen::MatrixXd::Zero(num_dimension, num_coeff);
  basis_matrices_.resize(num_segments);
  for (size_t i = 0; i < basis_matrices_.size(); i++) {
    basis_matrices_[i] = M(spline_order_, i + spline_order_ - 1);
  }
}
} // namespace bspline_pk