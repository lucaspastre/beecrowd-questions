A, B, C = map(int, input().split())
H, L = map(int, input().split())

if (C <= H and B <= L) or (A <= H and C <= L) or (A <= H and B <= L) or (B <= H and C <= L) or (C <= H and A <= L) or (B <= H and A <= L):
    print('S')

else:
    print('N')
