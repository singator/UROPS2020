import gzip
from lxml import etree as et
import os

# function to unzip xopp to xml
def UnzipXopp(fname):
    rootpt = os.getcwd()+'/'
    with gzip.open('{}Input/{}'.format(rootpt, fname)) as f:
        content = f.readlines()
        s = ''
        for line in content:
            newline = str(line)[2:-3]
            s += newline
    f.close()

    root = et.XML(s)
    with open('{}Input/'.format(rootpt) + fname.strip('.xopp') + '.xml', 'w') as newfile:
        newfile.write(et.tostring(root, xml_declaration=True).decode('utf-8'))
    newfile.close()

