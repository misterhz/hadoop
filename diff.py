import numpy as np

file_local = open('res_big.csv', 'r')
file_remote = open('res_cl.csv', 'r')

lines_local = [line for line in file_local]
lines_remote = [line for line in file_remote]

# for line in lines_local:
#     print(line.replace('\n', ''))

# for line in lines_local:
#     if line in lines_remote:
#         print(line.replace('\n', ''))

total_local = np.array([int(line.replace('\n', '').split('\t')[-1]) for line in lines_local]).sum()
total_remote = np.array([int(line.replace('\n', '').split('\t')[-1]) for line in lines_remote]).sum()

print(total_local)
print(total_remote)