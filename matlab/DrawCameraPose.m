% figure
% plot3
figure
hold on
grid on  
% xlim([-15,20]);
% ylim([-15,20]);
% zlim([15,25]);
for row=1:775
    R=rotationVectorToMatrix(pose(row, 2:4));
    c=-R'*pose(row, 5:7)';
    R=R';    
    cam = plotCamera('Location',c,'Orientation',R,'Opacity',0.0, 'Size', 0.07, 'color', [0, 0, 1]);
end
