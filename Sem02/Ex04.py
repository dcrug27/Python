wm = int(input())
max_wm = int(input("watermelon 0 -> "))
max_wm_i = 0
min_wm = max_wm
min_wm_i = 0

# for i in range(wm):
#     wm = int(input(f'watermelon {i} -> '))
#     wms.append(wm)

# print(min(wms))
# print(max(wms))

for i in range(1, wm):
    wm = int(input(f'watermelon {i} -> '))
    if wm > max_wm:
        max_wm = wm
        max_wm_i = i
    if wm < min_wm:
        min_wm = wm
        max_wm_i - i
 
print(min_wm, max_wm), (min_wm_i, max_wm_i)