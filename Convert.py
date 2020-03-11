
from bs4 import BeautifulSoup

# function to convert xml to scgink
def Convert(fname):
    name = fname.strip('.xml')
    with open('/home/wenhan/PycharmProjects/UROPS2020/Input/{}'.format(fname), "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        pages = {}
        pagenum = 0
        for tag in soup.find_all('page'):
            pages[pagenum] = {}
            stroke_counter = 0
            for stroke in tag.find_all('stroke'):
                text = str(stroke.text).split(' ')
                x = []
                y = []
                for i in range(len(text)):
                    if i % 2 == 0:
                        x.append(float(text[i]))
                    else:
                        y.append(float(text[i]))
                coordinates = {}
                coordinates['x'] = x
                coordinates['y'] = y
                pages[pagenum][stroke_counter] = coordinates
                stroke_counter += 1
            pagenum += 1
    f.close()

    # write strokes content into scgink format
    for num in pages.keys():
        output = '/home/wenhan/PycharmProjects/UROPS2020/SCG/{}_{}.scgink'.format(name, num)
        newf = open(output, "w+")
        newf.write('SCG_INK\n')
        allstrokes = pages[num]
        newf.write(str(len(allstrokes)) + '\n')
        for i in range(len(allstrokes)):
            stroke = allstrokes[i]
            pts = len(stroke['x'])
            newf.write(str(pts) + '\n')
            for j in range(pts):
                newf.write(str(stroke['x'][j]) + ' ' + str(stroke['y'][j]) + '\n')
        newf.close()
    return len(pages)
