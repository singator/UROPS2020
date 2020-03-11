import gzip
from lxml import etree as et


# function to unzip xopp to xml
def UnzipXopp(fname):
    with gzip.open('/home/wenhan/PycharmProjects/UROPS2020/Input/' + fname) as f:
        content = f.readlines()
        s = ''
        for line in content:
            newline = str(line)[2:-3]
            s += newline
    f.close()

    root = et.XML(s)
    with open('/home/wenhan/PycharmProjects/UROPS2020/Input/' + fname.strip('.xopp') + '.xml', 'w') as newfile:
        newfile.write(et.tostring(root, xml_declaration=True).decode('utf-8'))
    newfile.close()

