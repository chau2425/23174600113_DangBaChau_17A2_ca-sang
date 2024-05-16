def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    odd_numbers = filter(lambda x: x % 2 != 0, numbers)

    square_odd_numbers = map(lambda x: x**2, odd_numbers)

    square_odd_numbers_list = list(square_odd_numbers)

    print("Danh sách bình phương của các số lẻ:")
    print(square_odd_numbers_list)

if __name__ == "__main__":
    main()
