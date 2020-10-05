from triangle import check

def test():
    count = 1
    fin = open('input.txt', 'r', encoding='utf-8')
    fout = open('output.txt', 'w')
    for line in fin:
        line = line.strip()
        triangle_res = check(line.split(' '))
        line = fin.readline().strip()
        test_res = line
        if triangle_res == test_res:
            fout.write('Test ' + str(count) + ' success' + '\n')
        else:
            fout.write('Test ' + str(count) + ' error' + '\n')
        if not line:
            break
        count = count + 1
    fin.close()
    fout.close()

if __name__ == '__main__':
    test()
