import time



print("Bài tập 6.1: Giai thừa")
def giai_thua_de_quy(n):
    if n <= 1:  # Điều kiện dừng
        return 1
    return n * giai_thua_de_quy(n - 1)

def giai_thua_lap(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua

print("Bài tập 6.1 : Giai thừa bằng đệ quy")
print("Kết quả 5! (Đệ quy vs Lặp):", giai_thua_de_quy(5), "-", giai_thua_lap(5))

print("Bài tập 6.2: Fibonacci")
def fibonacci_de_quy(n):
    if n <= 1:  
        return n
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)


print("10 số Fibonacci đầu tiên:")
for i in range(10):
    print(fibonacci_de_quy(i), end=" ")
print("\n")


print("Đang tính fibonacci_de_quy(30)...")
bat_dau = time.time()
ket_qua_fib = fibonacci_de_quy(30)
ket_thuc = time.time()

print(f"Fibonacci(30) = {ket_qua_fib}")
print(f"Thời gian thực thi: {ket_thuc - bat_dau:.4f} giây")