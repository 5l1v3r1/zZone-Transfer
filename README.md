#zZone-Transfer

DNS域传送漏洞探测工具。多线程，批量探测，漏洞利用，简单网页采集。  
  
DNS zone transfer vulnerability Vulnerability detection tool  
support multithreading,batch scanning and vulnerability exploitation  
 
##get_url.py  
从[http://www.qkankan.com/](http://www.qkankan.com/)采集url并存储到target_list.txt中  
  
##zZone.py  
从target_list.txt导入url并进行测试，结果存储在 vulnerable_hosts.txt  
默认10线程  
  
#利用  
`> .\BIND9\dig.exe @dns01.benq.com axfr benq.com`  
该命令结果已被脚本自动存储到\dns\目录中
  
#参考  
[lijiejie/edu-dns-zone-transfer](https://github.com/lijiejie/edu-dns-zone-transfer)  
代码不多，拿过来基本没怎么改，向大师学习！  
  
[http://www.cdxy.me](http://www.cdxy.me/)  
mail: i@cdxy.me  
