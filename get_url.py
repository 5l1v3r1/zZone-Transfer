import re
import urllib

"""
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
"""
def getImg(html):
    reg = r'http://(.*?)(/|\"|\')'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist      
   
#html = getHtml("http://bank.elanw.com/")
#ans = getImg(html)
ans = getImg(open("aaa.txt").read())


fobj = open('target_list.txt','w')
ans_list = []
for each in ans:
	if each[0] not in ans_list:
		ans_list.append(each[0])
		fobj.write(each[0]+'\n')
fobj.close()
print "over! \n Targets:" + str(len(ans_list))