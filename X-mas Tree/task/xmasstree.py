def place_decorations(stars):
    lst = list(stars)

    # places 'O' in all possible spots to decorate the tree
    for i in range(0, len(lst)):
        if i % 2 == 1:
            lst[i] = 'O'

    return ''.join(lst)


def trim_decorations(tree, interval):
    lst = list(tree)
    counter = 0

    # checks for 'O' and replaces them with leaves if not part of the interval
    for i in range(0, len(tree)):
        if lst[i] == 'O':
            counter += 1
        if counter % interval != 1 and lst[i] == 'O' and interval != 1:
            lst[i] = '*'

    return ''.join(lst)


def create_tree(y):
    tree = ''
    for i in range(0, y):
        white_space = (y - i - 1) * ' '
        # place Christmas star and top
        if i == 0:
            tree += white_space + 'X' + '\n'
            line = '^'
        else:
            stars = ((1 + i * 2) - 2) * '*'
            stars = place_decorations(stars)
            line = '/' + stars + '\\'
        tree += white_space + line + '\n'

    # calculate trunk white space with formula
    trunk_white_space = ((y - 1) * 2 // 2 - 1) * ' '
    trunk = trunk_white_space + '| |'
    tree += trunk

    return tree


def create_empty_postcard(width=50, height=30):
    postcard = ''
    for i in range(0, height):
        for j in range(0, width):
            if i == 0 or i == height - 1:
                postcard += '-'
            elif (j == 0 or j == width - 1) and (i != 0 or i != height - 1):
                postcard += '|'
            else:
                postcard += ' '
        postcard += '\n'
    return postcard


def add_sentence(sentence, postcard, row=27):
    lst = postcard.splitlines()
    string_row = lst[row]

    # calculate the middle of the row
    if len(sentence) % 2 == 0:
        s = string_row[:len(string_row) // 2 - len(sentence) // 2] + sentence + string_row[
                                                                                len(string_row) // 2 + len(
                                                                                    sentence) // 2:]
    else:
        s = string_row[:len(string_row) // 2 - len(sentence) // 2] + sentence + string_row[
                                                                                len(string_row) // 2 + len(
                                                                                    sentence) // 2 + 1:]
    lst[row] = s
    return '\n'.join(lst)


def add_tree(postcard, tree, x, y, width=50):
    tree_lines = tree.splitlines()
    postcard_lst = list(postcard)
    prev_line = ''
    for line in tree_lines:
        line = line.lstrip()
        y -= len(line) - 1
        for c in line:
            coordinates = x * (width + 1) + y
            char = postcard[coordinates]
            if c == '|':
                coordinates -= (len(prev_line) // 2)  # get middle of the tree from previous line
            if char != '\n' and char != '-':
                postcard_lst[coordinates] = c
            if c != 'X':
                y += 1
        x += 1
        prev_line = line
    return ''.join(postcard_lst)


def main():
    # creating Xmas postcard
    postcard = create_empty_postcard()
    postcard = add_sentence("Merry Xmas", postcard)

    # parsing input
    inp = input().split()
    if len(inp) == 2:
        height, interval = int(inp[0]), int(inp[1])
        tree = trim_decorations(create_tree(height), interval)
        print(tree)
    else:
        for i in range(0, len(inp), 4):
            height = int(inp[i])
            interval = int(inp[i + 1])
            x = int(inp[i + 2])
            y = int(inp[i + 3])
            tree = trim_decorations(create_tree(height), interval)  # create tree with decorations
            postcard = add_tree(postcard, tree, x, y)
        print(postcard)


main()
