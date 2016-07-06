from xml.dom import minidom as mn
import urllib.request as u
import os

orgPath = '/Users/fahmidahamid/Desktop/buildDB/'
titlePath = orgPath + 'title'
absPath = orgPath + 'abs'
pdfPath = orgPath + 'pdfRepository'
paths = [titlePath, absPath, pdfPath]

for p in paths:
    try:
       os.stat(p)
    except:
       os.mkdir(p)       



xmldoc = mn.parse('oai2.xml')
recList = xmldoc.getElementsByTagName('arXiv')
print(len(recList))
for r in recList:
    id = r.getElementsByTagName('id')[0]
    title = r.getElementsByTagName('title')[0]
    abs = r.getElementsByTagName('abstract')[0]
    s_id = str(id.firstChild.data)
    print(s_id)
    title_str = str(title.firstChild.data)
    #input()
    abs_str = str(abs.firstChild.data)
    #input()
    download_url = 'http://arxiv.org/pdf/'+ s_id + '.pdf'
    response = u.urlopen(download_url)
    file = open(pdfPath +'/'+ s_id + ".pdf", 'wb')
    file.write(response.read())
    file.close()
    titleFile =  open(titlePath +'/'+ s_id + '.txt',  'w')
    titleFile.write(title_str)
    absFile = open(absPath + '/' + s_id + '.txt', 'w')
    absFile.write(abs_str)
    titleFile.close()
    absFile.close()
    print("Completed")
    
