aslsignkey = 1
aslsignclarifierkey = 1

separator = "|"

for i in range(97, 123):
    file_name = "%s.txt" % chr(i)
    asl_sign_file = open(file_name, "r")

    insert_aslsigns_query = ""
    insert_aslsignclarifiers_query = ""

    csv_data = ""

    for line in asl_sign_file:
	#if line doesn't begin with tab we know it's regular sign that doesn't have any clarifiers attached to it
	if line.strip():
	    if not line.startswith("\t"):
		line = line.split("\t")

		#insert_aslsigns_query += "INSERT INTO aslsigns(aslsignkey, sign, link) values(%s, %s, %s)\n" % (aslsignkey, line[0], line[1])
		new_csv_row = "%s %s %s %s %s\n" % (aslsignkey, separator, line[0], separator, line[1])
		if(len(new_csv_row.strip()) > 0):
		    csv_data += new_csv_row
		aslsignkey += 1

	    #not handling clarifying dictionary signs yet....
	    """
	    if line.startswith("\t"):
		insert_aslsignclarifiers_query += "INSERT INTO aslsiqn_clarifiers values()" % ()
		aslsignclarifierkey += 1
	    """

    #print insert_aslsigns_query


    #
    #
    #remove empty lines
    #
    #
    new_contents = []

    print csv_data[:100]

    # Get rid of empty lines
    for line in csv_data:
	#print line
	# Strip whitespace, should leave nothing if empty line was just "\n"
	if not line.strip():
	    continue
	# We got something, save it
	else:
	    new_contents.append(line)

    # Print file sans empty lines
    print "\n".join(new_contents)