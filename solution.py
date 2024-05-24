import pandas as pd
import numpy as np


chat_id = 1171143592 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    res = anderson_ksamp([x, y])
    return res.pvalue < 0.09
