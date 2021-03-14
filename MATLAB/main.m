close all
clear variables
%%
spectra = importdata("spectra.csv");
starNames = importdata("star_names.csv");
lambdaDelta = importdata("lambda_delta.csv");
lambdaStart = importdata("lambda_start.csv");
lambdaPredicted = 628.28; % Length of Halpha for H, nm
speedOfLight = 299792.458; % Speed of Light, km/s
%%
[nObs, nStars] = size(spectra);
lambda = [lambdaStart : lambdaDelta : lambdaStart + lambdaDelta * (nObs - 1)]';
%%
[sHa, idx] = min(spectra);
lambdaHa = lambda(idx);
z = (lambdaHa / 656.28) - 1;
speed = z * speedOfLight;
%%
fg1 = figure;
set(fg1, 'visible', 'on');
xlabel('Длина волны, мм')
ylabel(['Интенсивность, эрг/см^2/с/', char(192)])
grid on
hold on
for i = [1: nStars]
    if speed(i) > 0
        plot(lambda, spectra(:, i), 'LineWidth', 3);
    else
        plot(lambda, spectra(:, i), '--', 'LineWidth', 1)
    end
end
title('Спектры некоторых звезд')
legend(starNames)
movaway = starNames(speed > 0)
text(645, 3.2 * 10 ^ (-13), 'Кашапов Данир, Б04-001')
hold off
saveas(fg1, 'спектры.png')