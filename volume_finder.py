import streamlit as st

def find_closest_combination(target_volume, m_size=450, l_size=650):
    min_diff = float('inf')
    best_m = 0
    best_l = 0
    max_m = target_volume // m_size + 1
    max_l = target_volume // l_size + 1

    for m in range(max_m + 1):
        for l in range(max_l + 1):
            total = m * m_size + l * l_size
            diff = abs(target_volume - total)
            if diff < min_diff:
                min_diff = diff
                best_m = m
                best_l = l
                if diff == 0:
                    # Indent this return statement to be part of the if block
                    return best_m, best_l, total

    # This return statement was previously indented incorrectly
    return best_m, best_l, best_m * m_size + best_l * l_size

# Streamlit 介面 - This section was previously indented incorrectly
st.title("M/L 容器數量最佳組合計算器")
st.write("輸入總容量，我們幫你找出最接近的 M (450ml) 和 L (650ml) 組合")

target = st.number_input("請輸入目標總容量 (ml)", min_value=1, step=1)

if target:
    m, l, total = find_closest_combination(target)
    # Correct the typo from st.number_inpu to target
    st.success(f"最接近的組合：M = {m} 杯, L = {l} 杯，總容量 = {total} ml，偏差 = {total - target} ml")