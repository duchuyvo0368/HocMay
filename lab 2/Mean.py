import random


def calculate_mean(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    return mean


# Example usage

# Tạo danh sách 100.000 số nguyên ngẫu nhiên trong khoảng từ 1 đến 100000
numbers = [random.randint(1, 3) for _ in range(3)]

# In ra danh sách các số nguyên ngẫu nhiên
print(calculate_mean(numbers))
print(numbers)
