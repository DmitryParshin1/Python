# n = (1.96**2 * 0.015 * (1 - 0.015)) / 0.002**2
# print(n)

# n = (1.96**2 * 0.017 * (1 - 0.017)) / 0.002**2
# print(n)

import math

# def calculate_sample_size(ctr, confidence_level, power):
#     z_score = 2.58  # Значение Z-статистики для уровня доверия 99% и мощности 90%
#     p = ctr / 100.0

#     n = (z_score**2 * p * (1 - p)) / (p - ctr + z_score**2/4 * power)
#     return n

# current_ctr = 3.0  # Текущая конверсия в заказ в процентах
# expected_lift = 0.1  # Ожидаемое улучшение конверсии в процентах
# confidence_level = 99  # Уровень доверия в процентах
# power = 90  # Уровень мощности в процентах

# # Расчет размера выборки для текущей формы подтверждения заказа
# current_sample_size = calculate_sample_size(current_ctr, confidence_level, power)

# # Расчет размера выборки для новой формы подтверждения заказа
# new_sample_size = calculate_sample_size(current_ctr + expected_lift, confidence_level, power)

# print(f"Размер выборки для текущей формы подтверждения заказа: {current_sample_size}")
# print(f"Размер выборки для новой формы подтверждения заказа: {new_sample_size}")



# def calculate_sample_size(mean, expected_change, sd, confidence_level):
#     z_score = 1.96  # Значение Z-статистики для уровня доверия 95%
#     d = expected_change - mean

#     n = (z_score**2 * sd**2) / (d**2)
#     return n

# current_mean = 2167  # Текущий средний чек
# expected_change = 2180 - current_mean  # Ожидаемое изменение среднего чека
# sd = 69  # Стандартная ошибка (SD)
# confidence_level = 95  # Уровень доверия в процентах

# # Расчет размера выборки для текущей версии
# current_sample_size = calculate_sample_size(current_mean, expected_change, sd, confidence_level)

# # Расчет размера выборки для новой версии
# new_sample_size = calculate_sample_size(current_mean + expected_change, expected_change, sd, confidence_level)

# print(f"Размер выборки для текущей версии: {current_sample_size}")
# print(f"Размер выборки для новой версии: {new_sample_size}")


from scipy import stats

# Заданные значения
p_value = 0.00002
alpha = 0.05

# Проверка статистического вывода
if p_value < alpha:
    print("Отвергаем гипотезу о нормальности распределения")
else:
    print("Не отвергаем гипотезу о нормальности распределения")
