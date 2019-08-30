with open('ambassador.txt', 'r+') as file:
    data = file.read()
    list1 = data.split("\n")
    trucks = {}
    for entry in list1:
        key = entry.split(':')[0]
        dollars = float(entry.split(':')[1][:-4])
        if key not in trucks:
            trucks[key] = dollars
        if key in trucks:
            trucks[key] += dollars
    file.truncate(0)
    for key in sorted(trucks.keys()):
        file.write("%s: %s \n" % (key, trucks[key]))
    file.close()
