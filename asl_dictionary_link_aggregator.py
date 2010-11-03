from BeautifulSoup import BeautifulSoup, SoupStrainer
import urllib
import urlparse

url_base = "http://lifeprint.com/asl101/index/%s.htm"
asl_101_url = "http://lifeprint.com/asl101/"
delimiter = ", "

#get ascii values of lowercase english alphabet
#for i in range(97, 123):
for i in range(98, 99):
    curr_letter = chr(i)
    url = url_base % (curr_letter)

    page_content = urllib.urlopen(url).read()

    #grab all links
    link_strainer = SoupStrainer("a")
    l = [anchor for anchor in BeautifulSoup(page_content, parseOnlyThese=link_strainer)]

    #first item is just a placeholder link for the letter we're viewing
    #so remove it from the list
    l.remove(l[0])

    f = open(("%s.txt" % (curr_letter)), "w")
    prev_data = ""

    for anchor in l:
	link_fragment = anchor["href"]
	link_content = anchor.contents[0]

	print link_content

	#-1 if unable to parse content of link
	link_content = (link_content if link_content != None else "-1")

	link = urlparse.urljoin(asl_101_url, link_fragment)
	link_pattern = "http://lifeprint.com/pages-signs/"
	if link.startswith(link_pattern + curr_letter):
	    #write previous data since the next asl sign is not a "clarifier" for the previous sign
	    data = delimiter.join(prev_data)
	    f.write(data)

	    prev_data = [link_content, link]
	else:
	    prev_data.append(link_content)
	    prev_data.append(link)



	    if link.startswith(link_pattern + curr_letter):
		f.write("%s\t\t%s\n" % (link_content, link))
	    else:
		f.write("\t%s\n" % link)
    f.close()