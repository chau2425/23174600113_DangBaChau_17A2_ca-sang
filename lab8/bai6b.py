def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    print("Các số chẵn trong danh sách là:")
    print(even_numbers)

if __name__ == "__main__":
    main()
