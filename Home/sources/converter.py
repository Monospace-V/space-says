# Rough txt/md to html convertor.


def convert(data,trigger,tag,closed_trigger=True,close_tag=True):
    if not(closed_trigger):
        og_data=data
        if not(close_tag):
            data=data.split(trigger)
            data=data.join(tag)
            try: # Checking ends. If word too short, will break
                if og_data[0:len(trigger)+1]==trigger: data=tag+data
                if og_data[-len(trigger)-1:]==trigger: data=data+tag
            except: pass
            return data

        data.split() # if single-use triggers need closing. eg _word italicized -> <i>word</i> italicized.
        for i in range(len(data)):
            word=data[i]
            try: # check if word has trigger at start.
                word_st=word[0:len(trigger)+1]
                if wordst==trigger:
                    data[i]=word+trigger
            except: continue
        data="".join(data) # combine
        if og_data[0]==" ": data=" "+data
        if og_data[-1]==" ": data=data+" "
        # single use now converted to double use: Can now use in following
    tag_open=tag
    tag_close=tag[0]+"/"+tag[1:]
    while data.count(trigger)>=2: # converts in pairs
        for i in range(len(data)):
            if data[i:i+(len(trigger))]==trigger:
                data=data[0:i]+tag_open+data[i+(len(trigger)):]
                break
        for i in range(len(data)):
            if data[i:i+len(trigger)]==trigger:
                data=data[0:i]+tag_close+data[i+(len(trigger)):]
                break
    return data


filename=input("Enter name of file with extension: ")
out=input("Output file (exclude the extension): ")
out=out+".html"

with open(filename,'r') as file:
    text=file.read()

text=text.split("\n\n\n") # Split into paragraphs for <p>
header=text.pop(0).split("\n")
heading=header[0]
subtitle=header[1]
title=heading.upper()+" - space-says"

for parapos in range(len(text)): # Linebreak split for <br>
    para=text[parapos]
    para=para.split("\n")
    for line in para:
        if not line: para.remove(line)
    text[parapos]=para


# Time to format.
for para in text:
    for pos in range(len(para)):
        line=para[pos]
        line=convert(line,"**","<b>") # bold
        line=convert(line,"*","<i>") # italics
        line=convert(line,"```","<div class=\"code\">") # italics
        line=convert(line,"__","<b>",closed_trigger=False)
        line=convert(line,"_","<i>",closed_trigger=False)
        para[pos]=line


# Formatting anchors and links.
for para in text:
    citation=False # default
    for line_pos in range(len(para)):
        line=para[line_pos]
        for pos in range(len(line)):
            try:
                # Finds links and anchors them to themselves (max one link per line):
                if (line[pos:pos+4]=="http") and ("://" in line[pos+4:pos+8]): # Find link
                    link_end=line.find(" ",pos,-1) # returns -1 if not found, so last position anyway.
                    if link_end==-1: line+=" " # add space to prevent anchor href cutting
                    link=line[pos:link_end]
                    line=line[:pos]+"<a href=\""+link+"\">"+link+"</a>"+line[link_end:]
                    if link_end==-1: 
                        line=line[:-1] # Remove extra space
                        if pos==0 and citation==False: # Convert to citation: START
                            citation=True
                            line="<div class=\"citations\">\n"+line
                    para[line_pos]=line
                break
            except: pass
    if citation: para[line_pos]=line+"\n</div>" # CLOSE citations. only at end of para.

# Add with paragraph breaks.

start="""<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link href="../../Common/style.css" rel="stylesheet" type="text/css" media="all">
		<link href="../../Common/navbars.css" rel="stylesheet" type="text/css" media="all">
		<link href="../../Common/extra.css" rel="stylesheet" type="text/css" media="all">
		
"""

mid="""
	</head>
	<body class="global">
		<div class="navigator"><object data="../../Common/navigator.html"></object></div>

<div class="article">
"""

end="""
<p><object data="../../Common/common_footer.html"></object>
</div>
	</body>
</html>
"""
hr="""<hr class="separator">"""

with open(out,'w') as file:
    file.writelines([(start),("<title>"+title+"</title>"),(mid)])
    file.write("<div class=\"heading\">"+heading+"</div>\n")
    file.write("<div class=\"subtitle\">"+subtitle+"</div>\n\n")
    file.write(hr+"\n")
    for para in text:
        file.write("<p>\n")
        for line in para:
            file.write(line)
            if line!=para[-1]: file.write("<br>")
            file.write("\n")
    file.write(end)
