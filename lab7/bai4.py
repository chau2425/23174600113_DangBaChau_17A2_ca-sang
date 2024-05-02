# Khởi tạo từ điển inventory
inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Thêm key 'pocket' với giá trị là một danh sách
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# Sắp xếp các phần tử trong 'backpack'
inventory['backpack'].sort()

# Loại bỏ phần tử 'dagger' trong 'backpack'
if 'dagger' in inventory['backpack']:
    inventory['backpack'].remove('dagger')

# Thêm giá trị 50 vào 'gold'
inventory['gold'] += 50

# In ra inventory sau khi đã thực hiện các yêu cầu
print("Tài sản sau khi thực hiện các yêu cầu:")
print(inventory)
