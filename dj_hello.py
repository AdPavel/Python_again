# import random
# # print('Hello world')
# any_str = 'Hello Python!'
# print(any_str[3])
# print('Hello world'[3])
# print(any_str[0:2])
# print(any_str[0]+any_str[1])
# print(any_str[6] + 'a' + any_str[8:10])
# print('z'.upper()*5)
#
# print("""
# {:15.4f}{:15.4f}{:15.4f}{:15.4f}
# {:15.4f}{:15.4f}{:15.4f}{:15.4f}
# """.format(*[random.uniform(1, 2) for i in range(0, 9)]))

# ls = [1, 'hello', 1.3, 34, 'ertdf', [1, 2, 3]]
# ls1 = ls[:3]
# print(*ls1)

# tuple_note = 'hp', '8GB', '120gb', 'mouse', 'keyboard'
# note, ram, hdd, manip, board = tuple_note
# print(note, ram, hdd, manip, board)
# new_set = set(' '.join(['aaasdkjklhjhsssdhhh']))
# # new_ls = ' '.join(new_set)
#
# print(type(new_set.pop()))

# age = int(input('Enter you age: '))
# print('Access ' + str(age >= 18))

# x, y = 3, 4
# sym1, sym2 = 'a', 'A'
#
# print(sym1 == sym2)
# print(ord(sym1), ord(sym2))

# n = input('Enter number ')
# print(n + ' is even' if int(n) % 2 == 0 else n + ' is odd')

# print(*[n for n in range(10, 31) if n%2 == 0])
#
# print(sum([_ for _ in range(10, 31, 2)]))
#
# print(*['hello\n' for _ in range(int(input('Enter number ')))])

# import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec
# import math
# import numpy as np
#
# #### plot (4,4,5,5)
# data_4d = np.linspace(0, 1, 400).reshape((4,4,5,5))
# num_out_img, num_inner_img, img_w, img_h = data_4d.shape
#
# fig = plt.figure(1, figsize=(6, 6))
#
# outer_grid = math.ceil(math.sqrt(num_out_img))
# inner_grid = math.ceil(math.sqrt(num_inner_img))
#
# outer_frame = gridspec.GridSpec(outer_grid, outer_grid)
#
# for sub in range(num_out_img):
#
#     inner_frame = gridspec.GridSpecFromSubplotSpec(inner_grid, inner_grid, subplot_spec=outer_frame[sub], wspace=0.0, hspace=0.0)
#
#     for sub_sub in range(num_inner_img):
#
#         ax = plt.Subplot(fig, inner_frame[sub_sub])
#         ax.imshow(data_4d[sub, sub_sub, :, :], cmap='gray')
#         fig.add_subplot(ax)
#
# plt.show()
#
# #### plot (4,4,4,5,5)
# data_5d = np.linspace(0, 1, 1600).reshape((4,4,4,5,5))
# num_out_img, num_inner_img, num_deep_img, img_w, img_h = data_5d.shape
#
# fig = plt.figure(1, figsize=(6, 6))
#
# outer_grid = math.ceil(math.sqrt(num_out_img))
# inner_grid = math.ceil(math.sqrt(num_inner_img))
# deep_grid = math.ceil(math.sqrt(num_deep_img))
#
# outer_frame = gridspec.GridSpec(outer_grid, outer_grid)
#
# for sub in range(num_out_img):
#
#     inner_frame = gridspec.GridSpecFromSubplotSpec(inner_grid, inner_grid, subplot_spec=outer_frame[sub], wspace=0.0, hspace=0.0)
#
#     for sub_sub in range(num_inner_img):
#
#         deep_frame = gridspec.GridSpecFromSubplotSpec(deep_grid, deep_grid, subplot_spec=inner_frame[sub_sub], wspace=0.0, hspace=0.0)
#
#         for deep in range(num_deep_img):
#
#             ax = plt.Subplot(fig, deep_frame[deep])
#             ax.imshow(data_5d[sub, sub_sub, deep, :, :], cmap='gray')
#             fig.add_subplot(ax)
#
# plt.show()

txt = 'hello'
xtx = reversed(txt)
print(xtx)
print('Same new text')

print('This is a super new text')