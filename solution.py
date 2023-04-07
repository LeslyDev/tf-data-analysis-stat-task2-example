import pandas as pd
import numpy as np

from scipy.stats import erlang


chat_id = 623406448 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = p
    loc = x.mean()
    return (loc + 0.5 - erlang.ppf(alpha / 2, len(x), loc=0, scale=1 / len(x))) / 14, \
           (loc + 0.5 - erlang.ppf(1 - alpha / 2, len(x), loc=0, scale=1 / len(x))) / 14
