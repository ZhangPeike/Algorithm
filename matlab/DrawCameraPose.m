figure
hold on
grid on
% xlim([-15,20]);
% ylim([-15,20]);
% zlim([15,25]);
c = -R' * t;
R = R';
cam = plotCamera('Location', c, 'Orientation', R, 'Opacity', 0.0, 'Size', 0.07, 'color', [0, 0, 1]);