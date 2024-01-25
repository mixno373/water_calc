import math
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as mfm

from io import BytesIO
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
from enum import Enum



# КОНСТАНТЫ
BOTTLE_COST = 36 # рублей, Бутылка воды 1 литр
FILTER_JUG_COST = 840 # рублей, Фильтр-Кувшин
FILTER_CASSETE_COST = 250 # рублей, 1 сменный фильтр
FILTER_1L_COST = 0.02515 # рублей, Стоимость 1 литра воды из крана

# УСЛОВИЯ СМЕНЫ ФИЛЬТРА
FILTER_JUG_LIFE = 3*365 # дней, Время жизни одного кувшина, 3 года
FILTER_CASSETE_LIFE = 350 # литров, Время жизни одного сменного фильтра на 1 человека в литрах фильтрованной воды

DAYLY_CONSUMPTION = 2 # литров, Дневное потребление воды
PEOPLE_COUNT = 2 # человек, Количество человек, использующих фильтр


# Расчет стоимости Бутылей и Фильтров за [day] дней
def calc_water_cost(day):
    # Всего использовано литров воды из крана
    all_liters = day * PEOPLE_COUNT * DAYLY_CONSUMPTION
    
    # Расчет стоимости Бутылей
    sum_of_bottle = day * BOTTLE_COST * DAYLY_CONSUMPTION
    
    # Расчет стоимости Фильтров
    # Посчитаем стоимость воды
    sum_of_filter = all_liters * FILTER_1L_COST
    # Добавим стоимость самого кувшина
    sum_of_filter = sum_of_filter + math.ceil(day / FILTER_JUG_LIFE) * FILTER_JUG_COST
    # Добавим стоимость сменных фильтров
    sum_of_filter = sum_of_filter + math.ceil(all_liters / FILTER_CASSETE_LIFE) * FILTER_CASSETE_COST
    
    return sum_of_bottle, sum_of_filter
    
    
    
plt.rcParams.update({'figure.max_open_warning': 0})

# Сбор данных для графика
bottle_plt_values = []
filter_plt_values = []
days_plt_values = []
days = 5 * 365 # Количество дней

# Рассчитываем данные
for day in range(1, days+1):
    sum_b, sum_f = calc_water_cost(day)
    bottle_plt_values.append(sum_b)
    filter_plt_values.append(sum_f)
    days_plt_values.append(day)

        
        
fig, ax = plt.subplots(figsize=(9, 4.5))
plt.margins(x=0.01, y=0.01)
plt.box(on=None)

# Добавляем данные в график
ax.plot(days_plt_values, bottle_plt_values, color="#62acd8", linewidth=1.5, label="Бутыли")
ax.plot(days_plt_values, filter_plt_values, color="#be7858", linewidth=1.5, label="Фильтр")
ax.axis([days_plt_values[0]-1, days_plt_values[-1]+1, min(min(*bottle_plt_values), min(*filter_plt_values))-1, max(max(*bottle_plt_values), max(*filter_plt_values))+1])
ax.legend()

plt.yticks(color="#FFFFFF")
plt.xticks(color="#FFFFFF")
ax.set_axisbelow(True)
# ax.grid(b=True, axis='both', color="#313237")
# ax.tick_params(axis='y', which='both', left=False, bottom=False, top=False, labelleft=False, labelbottom=False)
fig.tight_layout()
ax.set_facecolor('#36393f')
fig.patch.set_facecolor('#36393f')

# Конвертировать график в объект изображения
f_name = f"plot.png"
img_buf = BytesIO()
plt.savefig(img_buf, format='png', facecolor=fig.get_facecolor(), transparent=True)
plt.clf()
fig.clf()
ax.cla()
plot_img = Image.open(img_buf)

plot_img.save(f_name, "PNG")