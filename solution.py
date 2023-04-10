import pandas as pd
import numpy as np


chat_id = 706100023 # Ваш chat ID, не меняйте название переменной

def solution(data1: int, 
        data2: int)-> bool:
  from scipy.stats import t
  # Вычисление средних значений и стандартных отклонений
  mean1 = np.mean(data1)
  mean2 = np.mean(data2)
  std1 = np.std(data1, ddof=1)
  std2 = np.std(data2, ddof=1)

  # Вычисление статистического показателя
  n1 = len(data1)
  n2 = len(data2)
  t_stat = (mean1 - mean2) / np.sqrt((std1**2 / n1) + (std2**2 / n2))

  # Вычисление критического значения
  alpha = 0.05
  df = n1 + n2 - 2
  critical_value = t.ppf(1 - alpha, df)

  # Проверка гипотезы
  if t_stat > critical_value or t_stat < -critical_value:
    rez = 1 # да отклонить нулевую гипотезу
  else:
    rez = 0 # нет, не отверганем, нулевая остается, не отклонять
  return bool(rez)
