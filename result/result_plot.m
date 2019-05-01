clc
clear
close all
%% select sequence
idx = 2;
seq_list = {"00", "05", "08"};
res_file_list = {'result00.txt', 'result05.txt', 'result08.txt'};
time_end_list = [426, 217, 537];

seq = seq_list{idx};
res_file = res_file_list{idx};
time_end = time_end_list(idx);
groundTruthFile= strcat(seq, '.txt');

%% Ground truth results
fileID = fopen(groundTruthFile, 'r');
b = fscanf(fileID, '%f'); %read data as floats
temp = reshape(b,[12 length(b)/12])';
% 
groundTruth = [temp(:,4) temp(:,8) temp(:,12)];
fclose(fileID);

%% Simulation Result
fileID = fopen(res_file, 'r');
b = fscanf(fileID, '%f'); %read data as floats
temp = reshape(b,[3 (length(b)/3)])';
X2_gt_ros = -temp(:,1);
Z2_gt_ros = temp(:,2);
Y2_gt_ros = temp(:,3);


fclose(fileID);




%% plot data
figure1 = figure(1);
plot(X2_gt_ros, Y2_gt_ros, 'r'); hold on;
plot(groundTruth(:,1), groundTruth(:,3), 'b'); hold on;
legend('Odometry Result', 'Ground Truth', 'Location', 'NorthWest');
title(strcat('Kitti Result of Sequence', seq));
saveas(figure1,strcat(seq, '_cmp.png'));


%% Error and Comparison
resultX = X2_gt_ros;       % ;
resultY = Y2_gt_ros;       % ;

fprintf("result %d, ground truth %d", time_end, size(groundTruth, 1));
time_gt = linspace(0, time_end, size(groundTruth, 1));
time_res = linspace(0, time_end, length(resultX));
resultX = interp1(time_res, resultX, time_gt, 'Linear');
resultY = interp1(time_res, resultY, time_gt, 'Linear');
error_pos = sqrt((resultX' - groundTruth(:,1)).^2 + (resultY' - groundTruth(:,3)).^2);

figure2 = figure(2);
error_pos_mean = mean(error_pos);
error_pos_print = sprintf(': Error of Odometry, Average Error = %.2f m', error_pos_mean);
error_pos_print = strcat(strcat('Sequence', seq), error_pos_print);
plot(time_gt, error_pos);
xlabel('time [s]');
ylabel('Position Error [m]');
title(error_pos_print);
saveas(figure2,strcat(seq, '_error.png'));

end