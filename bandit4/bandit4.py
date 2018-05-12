fn = '-file0';
n = 0;

while n<10:
    newfn = fn + str(n);
    f = open(newfn, 'r')
    print "File 0"+str(n)
    print f.read()
    f.close
    n+=1