import csv

PATH = 'characters.txt'
OUT = 'clean_chars.txt'

if __name__ == '__main__':

    f = open(PATH,'r')

    reader = f.read()

    line_list = reader.split('\n')

    fullnames = []

    for line in line_list:
        if len(line) > 1:
            if '–' in line:
                fullname = line.split('–')[0].lower()
            elif '-' in line:
                fullname = line.split('-')[0].lower()
            else:
                print('borked: ',line)
            fullname = fullname.replace('/',' ')
            fullname = fullname.replace('the ','')
            fullname = fullname.replace('a.k.a.',' ')
            fullname = fullname.replace('(','')
            fullname = fullname.replace(')','')
            fullname = fullname.replace(',','')
            fullname = fullname.replace('.','')
            fullname = fullname.replace('"','')
            fullname = fullname.replace('-',' ')
            fullname = fullname.replace('née',' ')
            fullname = fullname.replace('born',' ')
            fullnames.append(fullname.strip())

    singles = set()

    for fullname in fullnames:
        namelist = fullname.split()
        for name in namelist:
            singles.add(name + '\n')

    o = open(OUT,'w')

    for line in singles:
        o.write(line)
    o.close()
