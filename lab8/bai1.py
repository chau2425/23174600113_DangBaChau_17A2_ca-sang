def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to_sinh_doi(duoi_han):
    so_nguyen_to_sinh_doi = []
    for i in range(2, duoi_han - 1):
        if la_so_nguyen_to(i) and la_so_nguyen_to(i + 2):
            so_nguyen_to_sinh_doi.append((i, i + 2))
    return so_nguyen_to_sinh_doi

# Tìm và in các số nguyên tố sinh đôi nhỏ hơn 1000
duoi_han = 1000
so_nguyen_to_sinh_doi = tim_so_nguyen_to_sinh_doi(duoi_han)
for cap in so_nguyen_to_sinh_doi:
    print(cap)
