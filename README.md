# Diffie-Hellman-Key-Exchange
Implement Diffie-Hellman Key Exchange with python

## Illustration
```
Diffie-Hellman-Parameters:
prime p (512 bits，hex):
00:9f:db:8b:8a:00:45:44:f0:04:5f:17:37:d0:ba:
2e:0b:27:4c:df:1a:9f:58:82:18:fb:43:53:16:a1:
6e:37:41:71:fd:19:d8:d8:f3:7c:39:bf:86:3f:d6:
0e:3e:30:06:80:a3:03:0c:6e:4c:37:57:d0:8f:70:
e6:aa:87:10:33
base element : g= 2
```

Notes:
- User Input (a, b)
- both a,b are hex
- For example: 9a4fee3c297b
- Output: (A, 𝑇𝐴), (B, 𝑇𝐵), (𝐾𝐴, 𝑇𝑘𝐴), and (𝐾𝐵, 𝑇𝑘𝐵)
  - $A=𝑔^𝑎𝑚𝑜𝑑𝑝$, 𝑇𝐴 = Spending time to calculate A(ms)
  - $B= 𝑔^𝑏𝑚𝑜𝑑 𝑝$, 𝑇𝐵 = Spending time to calculate B(ms)
  - 𝐾𝐴: Diffie-Hellman Key computed via B and A, 𝑇𝐾𝐴 = Spending time to calculate KA(ms)
  - 𝐾𝐵: Diffie-Hellman Key computed via A and B, 𝑇𝐾𝐵 = Spending time to calculate KB(ms)

## Documents

1. shared_secret.py: simply code to implement Diffie-Hellman Key Exchange
2. Diffie.py: for this situation to display the public value, share_secret and spending time

## Output
![Diffie.py output](https://github.com/Rita94105/Diffie-Hellman-Key-Exchange/blob/master/img/output.png)
