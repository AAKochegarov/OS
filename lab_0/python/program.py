n = []
f = open("data.txt")
for line in f.readlines():
    if(int(line) > 0 and int(line) < 32767):
        n.append(int(line))
        n.sort()
        b = 0
        print("Soobschenie " + str(n[0]) + "-" + str(n[len(n) - 1]), end = "")
        for i in range(n[0], n[len(n) - 1]):
            if n.count(i) == False:
                b = b + 1
                if b == 1:    
                    print(" nehvataet pacetov", end = " ")
                print(" " + str(i), end = "")
        if b == 0:
            print(" polucheno uspeshno", end = "")
        print("")
