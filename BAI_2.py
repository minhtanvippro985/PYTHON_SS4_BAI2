total_profit = 0
average_profit = 0
count_profit = 0

for days in range(1,8):
    profit = int(input(f"Nhập doanh thu ngày {days}"))
    total_profit = total_profit + profit
    if profit >= 5_000_000:
        count_profit = count_profit + 1
    
print(f"""
    ===== BÁO CÁO DOANH THU TUẦN RIKKEI STORE ====
    Tổng doanh thu cả tuàn {int(total_profit)} VND
    Doanh thu trung binh mỗi ngày {int(total_profit / 7)} VND
    Số ngày đạt doanh thu mục tiêu (> 5.000.000 VND) : {count_profit} NGÀY
    """)