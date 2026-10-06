# 破冰与转化率计算器
def calculate_rate(total, replied):
    rate = (replied / total) * 100
    print(f"发送: {total} | 回复: {replied} | 转化率: {rate:.2f}%")

calculate_rate(15, 2)
