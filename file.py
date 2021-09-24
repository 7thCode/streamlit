with open('source.txt') as read_fp:
    with open('dist.txt', 'a') as write_fp:
        write_fp.write(read_fp.read())