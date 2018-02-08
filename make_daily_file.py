import xml.etree.ElementTree as et

data={}
tree=et.parse("Data/00-04.xml")
root=tree.findall("host")

for host in root:
	 stime=host.get("starttime")       
	 etime=host.get("endtime")
	 ipv4_node=host.findall(".//address[@addrtype='ipv4']")
	 ipv4 = et.tostring(ipv4_node, encoding='utf8', method='xml')
	 print(stime,etime,ipv4)
