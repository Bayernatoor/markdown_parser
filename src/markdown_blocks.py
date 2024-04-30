def markdown_to_blocks(markdown):
    line_split = markdown.splitlines()
    temp_str = ""
    new_list = []
    for e in range(1, len(line_split)):
        if line_split[e] != "":
            temp_str += line_split[e] + "\n"
        if line_split[e] == "" or e + 1 >= len(line_split):
            if temp_str != "":
                new_list.append(temp_str.strip())
            temp_str = ""

    return new_list

#def markdown_to_blocks(markdown):
#    blocks = markdown.split("\n\n")
#    filtered_blocks = []
#    for block in blocks:
#        if block == "":
#            continue
#        block = block.strip()
#        filtered_blocks.append(block)
#    return filtered_blocks
