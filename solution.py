import pandas as pd
import numpy as np
# from scipy.stats import norm

chat_id = 506238275  # Ваш chat ID, не меняйте название переменной


def solution(control_sales: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    control_suc_rate = control_sales / x_cnt
    test_suc_rate = y_success / y_cnt
    z = (test_suc_rate - control_suc_rate) / (
            (control_suc_rate * (1 - control_suc_rate) * (1 / x_cnt + 1 / y_cnt)) ** 0.5)
    # z_critical = norm.ppf(1 - 0.08)
    z_critical = 1.4050715603096329

    return z > z_critical

# print(norm.ppf(1 - 0.08))
