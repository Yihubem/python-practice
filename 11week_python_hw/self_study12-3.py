import threading

def calc_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"1+2+3+...+{n} = {total}")

t1 = threading.Thread(target=calc_sum, args=(1000,))
t2 = threading.Thread(target=calc_sum, args=(100000,))
t3 = threading.Thread(target=calc_sum, args=(10000000,))

t1.start()
t2.start()
t3.start()

t1.j
