def reverse(path):
    with open(path) as f:
        number_str = f.read().strip()
    reverse_number = number_str[::-1]
    return reverse_number
print(reverse("linh.txt"))