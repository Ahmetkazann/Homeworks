test_giris = randi([-5,5], 50, 1);
test_giris2 = randi([-5,5], 50, 1);

fonksiyon = @(x) x.^4 - 16*x.^2 + 5*x;

test_cikis = (fonksiyon(test_giris) + fonksiyon(test_giris2)) / 2;

birlesik_tablo = [test_giris, test_giris2, test_cikis];  
dosya_klasoru = 'C:\Users\ahmet\Desktop\bulanık mantık';

dosya_adi = 'MyFis.fis';

% Fuzzy mantık sistem dosyasının tam yolu
fisDosyaYolu = fullfile(dosya_klasoru, dosya_adi);
fisObjesi = readfis(fisDosyaYolu);

fuzzy_cikis = evalfis([test_giris, test_giris2], fisObjesi);

birlesik_tablo = [birlesik_tablo, fuzzy_cikis];

disp('Birleşik Tablo:');
disp(birlesik_tablo);

train_giris = randi([-5,5], 75, 1);
train_giris2 = randi([-5,5], 75, 1);

gercek_cikislar = (fonksiyon(train_giris) + fonksiyon(train_giris2)) / 2;
anfis_model = anfis([[train_giris, train_giris2], gercek_cikislar]);
test_giris_verileri = [test_giris,test_giris2];
tahmini_cikislar = evalfis(test_giris_verileri, anfis_model);

birlesik_tablo = [birlesik_tablo, tahmini_cikislar];

anfistablo = [train_giris, train_giris2, gercek_cikislar];

sutun_3 = birlesik_tablo(:, 3);
sutun_4 = birlesik_tablo(:, 4);
sutun_5 = birlesik_tablo(:, 5);


figure;

scatter(1:numel(sutun_3), sutun_3, 'r', 'filled');
hold on;

p_3 = polyfit(1:numel(sutun_3), sutun_3, 1);
y_fit_3 = polyval(p_3, 1:numel(sutun_3));
plot(1:numel(sutun_3), y_fit_3, 'r-', 'LineWidth', 2);

scatter(1:numel(sutun_4), sutun_4, 'g', 'filled');

p_4 = polyfit(1:numel(sutun_4), sutun_4, 1);
y_fit_4 = polyval(p_4, 1:numel(sutun_4));
plot(1:numel(sutun_4), y_fit_4, 'g-', 'LineWidth', 2);

scatter(1:numel(sutun_5), sutun_5, 'b', 'filled');

p_5 = polyfit(1:numel(sutun_5), sutun_5, 1);
y_fit_5 = polyval(p_5, 1:numel(sutun_5));
plot(1:numel(sutun_5), y_fit_5, 'b-', 'LineWidth', 2);


xlabel('Veri Noktaları');
ylabel('Değerler');
title('3. 4. ve 5. Sütunların Grafiği');

legend('y_gercek', 'Eğim 3', 'y_MyFis', 'Eğim 4', 'Y_anfisToolBox', 'Eğim 5');

hold off;



