read = open('in.txt','r+')
write = open('out.txt','w')

for i in read:
    i = list(map(int,i.split()))
    i = [j**2 for j in i]

    for k in i:
        write.write(str(k)+' ')
    write.write('\n')
