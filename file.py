f = open('test.txt', 'a')
for i in range(100):
    f.write(str(i) + '\n')
f.close()