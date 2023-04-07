import pandas as pd
import numpy as np


chat_id = 1004689536 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    import math
    n = len(x)
    ln_x = [math.log(i) for i in x]
    a = math.exp(1/n * sum(ln_x) - math.log(431))
    return a # Ваш ответ
