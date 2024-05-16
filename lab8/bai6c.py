def main():
    numbers = [1, 2, 3, 4, 5]

    cube_list = list(map(lambda x: x**3, numbers))

    print("Danh sách lập phương:")
    print(cube_list)

if __name__ == "__main__":
    main()
