def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_numbers = filter(lambda x: x % 2 == 0, numbers)

    cube_even_numbers = map(lambda x: x**3, even_numbers)

    cube_even_numbers_list = list(cube_even_numbers)

    print("Danh sách lập phương của các số chẵn:")
    print(cube_even_numbers_list)

if __name__ == "__main__":
    main()
