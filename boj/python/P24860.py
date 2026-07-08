# https://www.acmicpc.net/problem/24860
# 2025-09-03 / 24860. Counting Antibodies / Bronze IV

V_k, J_k = map(int, input().split())
V_l, J_l = map(int, input().split())
V_h, D_h, J_h = map(int, input().split())

print((V_k * J_k + V_l * J_l) * (V_h * D_h * J_h))
