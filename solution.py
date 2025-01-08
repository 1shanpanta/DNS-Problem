from math import pow
def verify_2025():
    # Using the formula: 3^(4 * (2 - 1)) * 5^2
    result = pow(3, 4 * (2 - 1)) * pow(5, 2)
    return result

if __name__ == "__main__":
    print("The result is:", int(verify_2025())) 