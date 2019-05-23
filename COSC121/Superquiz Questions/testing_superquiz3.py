def tagged_contents(tag_name, lines):
    if "<" not in tag_name:
        start_tag = "<" + tag_name + ">"
        end_tag = "</" + tag_name + ">"
    startline = tag_position(start_tag, lines)
    endline = tag_position(end_tag, lines)    
    indexes = []
    for line in lines:
        if tag_name in line:
            indexes.append(lines.index(line))
    startindex = indexes[0]
    endindex = indexes[1]
    tagged = lines[startindex + 1:endindex]
    return tagged

    
def tag_position(tag, lines):
    """Returns the position of a tag to ensure which lines are headers with name and account info,
       and which are data lines with the band and amouint info"""    
    for line in lines:
        if line.startswith(tag):
            line_index = lines.index(line)  # Start line index
            return line_index            
    return -1

lines = ["<data>",
         "included",
         "also included",
         "</data>",
         "not included also"
         ]


def tagged_contents(tag_name, lines):
    if "<" not in tag_name:
        start_tag = "<" + tag_name + ">"
        end_tag = "</" + tag_name + ">"
        startline = tag_position(start_tag, lines)
        endline = tag_position(end_tag, lines)
        indexes = [startline, endline]
        tagged = lines[startline + 1:endline]
        return tagged
    elif "<" in tag_name and "/" in tag_name:
        start_tag_new = tag_name.replace("/", "")
        startline = tag_position(start_tag_new, lines)
        endline = tag_position(tag_name, lines)
        indexes = [startline, endline]
        tagged = lines[startline + 1:endline]
        return tagged    
    elif "<" in tag_name and "/" not in tag_name:
        end_tag_new = tag_name.strip("<")
        end_tagg = "</" + end_tag_new
        startline = tag_position(tag_name, lines)
        endline = tag_position(end_tagg, lines)
        indexes = [startline, endline]
        tagged = lines[startline + 1:endline]
        return tagged    

print(tagged_contents("data", lines))

