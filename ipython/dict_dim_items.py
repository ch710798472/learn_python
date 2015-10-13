import csv
fh = open ( '/home/ch/ipython/cat_id_matchsets.txt', 'w' ) 
f = open('/home/ch/ipython/outofid_matchsets.txt')
rate1 = open('/home/ch/taobao/dim_items.txt')

dic = dict()
for line in rate1:
    line = line.strip().split(' ')
    dic[line[0]] = [line[1],line[2]]

data = csv.reader(f,delimiter=';')
for l in data:
    for li in l:
        if(dic.has_key(li)):
            fh.write(dic[li][0]+' ')
    fh.write('\n')
print 'write OK\n'
