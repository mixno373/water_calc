# Расчет разницы стоимости воды в Бутылках и в Фильтре

## В чем суть?
Посчитать разницу затрат на покупку питьевой воды бутылками по 1 литру
с покупкой фильтра в кувшине со сменными кассетами.
  
Для анализа написан скрипт на языке Python с использованием библиотеки MatPlotLib для отрисовки визуальных графиков.

## Анализ

Исходные данные:
> - Норма воды в день на человека 2 литра
> - В семье есть еще 1 человек, использующий фильтр (только для расчета времени жизни сменной кассеты фильтра)
> - Срок жизни фильтра - 3 года
> - Срок жизни сменной кассеты - 350 литров
> - Значения цен взяты усредненно на Январь 2024г.
  
График затрат за первые 150 дней:
![График](https://github.com/mixno373/water_calc/blob/main/plot%20-%20150%20%D0%B4%D0%BD%D0%B5%D0%B9.png?raw=true)
  
График затрат за 1 год:
![График](https://github.com/mixno373/water_calc/blob/main/plot%20-%20365%20%D0%B4%D0%BD%D0%B5%D0%B9.png?raw=true)
  
График затрат за 5 лет:
![График](https://github.com/mixno373/water_calc/blob/main/plot%20-%205%20%D0%BB%D0%B5%D1%82.png?raw=true)

## Итоги

Начиная с 16 дня сумма затрат на бутылки с водой начинает превышать затраты на фильтрованную воду из крана.
Даже в динамике 5 лет затраты на фильтр и сменные кассеты значительно меньше затрат на покупку бутилированной воды.