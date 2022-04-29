data_read_01 = open ('01.txt', 'r')
data_read_02 = open ('02.txt', 'r')
data_write = open ('03.txt', 'a')

for read_01 in data_read_01:
    for read_02 in data_read_02:
        data_write.writelines(read_01)
        data_write.writelines('+')
        data_write.writelines(read_02)