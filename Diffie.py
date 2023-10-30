import time

a = input("\nEnter a as the first hexadecimal value: ")
b = input("Enter the second hexadecimal b value: ")

base = 2
exponent = "9a4fee3c297b"
modulus = 0x009fdb8b8a004544f0045f1737d0ba2e0b274cdf1a9f588218fb435316a16e374171fd19d8d8f37c39bf863fd60e3e300680a3030c6e4c3757d08f70e6aa871033

start_time_a = time.time() * 1_000_000
A = pow(base, int(a, 16), modulus)
end_time_a = time.time() * 1_000_000
elapsed_time_a = end_time_a - start_time_a
print("\nA:", hex(A))
print("TA:", elapsed_time_a, "microseconds")

start_time_b = time.time() * 1_000_000
B = pow(base, int(b, 16), modulus)
end_time_b = time.time() * 1_000_000
elapsed_time_b = end_time_b - start_time_b
print("\nB:", hex(B))
print("TB:", elapsed_time_b, "microseconds")

start_time_ka = time.time() * 1_000_000
shared_secret_A = pow(B, int(a, 16), modulus)
end_time_ka = time.time() * 1_000_000
elapsed_time_ka = end_time_ka - start_time_ka
print("\nKA:", hex(shared_secret_A))
print("TKA:", elapsed_time_ka, "microseconds")

start_time_kb = time.time() * 1_000_000
shared_secret_B = pow(A, int(b, 16), modulus)
end_time_kb = time.time() * 1_000_000
elapsed_time_kb = end_time_kb - start_time_kb
print("\nKB:", hex(shared_secret_B))
print("TKB:", elapsed_time_kb, "microseconds")
