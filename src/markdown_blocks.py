import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


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


def block_to_block_type(markdown_block):
    heading = re.findall(r'^#{1,6}\s.+', markdown_block)
    code_quote = re.findall(r'^\`{3,}.+\`{3,}$', markdown_block)
    quote_matches = re.finditer(r'^(>[^\n]*)(?:\n>|$)', markdown_block)
    # Extract individual strings from matches, excluding the newline character
    quote = [match.group(1) for match in quote_matches]
    unordered_list = re.findall('^[-*]{1} .+', markdown_block)
    ordered_list = re.findall(r'\d+\..+?(?=\n\d+\.|\Z)', markdown_block, re.DOTALL)
    # ensure each line increments by 1 (is ordered list)
    incrementing = all(int(ordered_list[i].split(".")[0]) == i + 1 for i in range(len(ordered_list)))

    if len(heading) > 0:
        return block_type_heading
    elif len(code_quote) > 0:
        return block_type_code
    elif len(quote) > 0:
        return block_type_quote
    elif len(unordered_list) > 0:
        return block_type_unordered_list
    elif incrementing:
        increments = [line.strip() for line in ordered_list]
        if len(increments) > 0:
            return block_type_ordered_list
        else:
            return block_type_paragraph

    return block_type_paragraph
