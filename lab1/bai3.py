def main():
    # Số tiền ban đầu
    initial_amount = 10000

    # Lãi suất hàng năm (tính theo tỷ lệ phần trăm)
    interest_rate = 0.06

    # Số năm
    years_5 = 5
    years_10 = 10

    # Tính toán số tiền sau 5 năm và 10 năm
    amount_after_5_years = initial_amount * (1 + interest_rate) ** years_5
    amount_after_10_years = initial_amount * (1 + interest_rate) ** years_10

    # Tính tỷ lệ tăng trưởng
    growth_rate = (amount_after_10_years - amount_after_5_years) / amount_after_5_years

    # In kết quả
    print("Số tiền sau 5 năm là:", round(amount_after_5_years, 2))
    print("Số tiền sau 10 năm là:", round(amount_after_10_years, 2))
    print("Tỷ lệ tăng trưởng sau 10 năm so với sau 5 năm là:", round(growth_rate, 2))

if __name__ == "__main__":
    main()