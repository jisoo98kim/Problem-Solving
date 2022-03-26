# Link: https://www.acmicpc.net/source/41109869

x, y, w, h = map(int, input().split())
print(min(x, y, w - x, h - y))

