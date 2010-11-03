from BeautifulSoup import BeautifulSoup, SoupStrainer
import urllib
import urlparse

url_base = "http://lifeprint.com/asl101/index/%s.htm"
asl_101_url = "http://lifeprint.com/asl101/"
delimiter = ", "

#get ascii values of lowercase english alphabet
for i in range(97, 123):
#for i in range(98, 99):
    curr_letter = chr(i)
    url = url_base % (curr_letter)

    page_content = urllib.urlopen(url).read()

    #grab all links
    link_strainer = SoupStrainer("a")
    links = [anchor for anchor in BeautifulSoup(page_content, parseOnlyThese=link_strainer)]

    #first item is just a placeholder link for the letter we're viewing
    #so remove it from the list
    links.remove(links[0])

    f = open(("%s.txt" % (curr_letter)), "w")
    curr_link_data = ""
    file_output = ""

    for anchor in links:
	link_is_clarifier = False
	link_fragment = anchor["href"]
	link_name = anchor.contents[0]

	#-1 if unable to parse content of link
	if(link_name == None):
	    link_name = "-1"
	else:
	    link_name = str(link_name).strip().replace('\r', '').replace('\n', '')
	    print link_name

	link = urlparse.urljoin(asl_101_url, link_fragment)
	link_pattern = "http://lifeprint.com/pages-signs/"

	#if link follows pattern then we know it's not a special "clarifier" link...
	if link.startswith(link_pattern + curr_letter):
	    #write previous data since the next asl sign is not a "clarifier" for the previous sign
	    curr_link_data = [link_name, link]

	#link doesn't follow pattern so we assume it's a "clarifier" link...
	#and is part of the existing link definition...
	else:
	    link_is_clarifier = True

	#write link_name, and link
	if (not link_is_clarifier):
	    f.write("%s\t\t%s\n" % (link_name, link))
	#write link_name and link but prepend with /t so we know it's a clarifier
	else:
	    #print "clarifier: %s" % link
	    f.write("\t%s\n" % link)
    f.close()