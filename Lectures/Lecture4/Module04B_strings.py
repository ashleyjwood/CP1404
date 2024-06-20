# Answer and then run in console
# text = "python"
# text[0:4]     -> "pyth"   -> correct
# text[4:7]     -> "on"     -> correct
# text[0:-4]    -> "hon"    -> wrong    -> "py"
# text[0::2]    ->          -> n/a      -> "pto" prints only every second chara, [0::3) would print only every third
# text[2:]      -> "thon"   -> correct


def main():
    """Extract name-value pairs as tuples in a list from a query string."""
    # query_string = "?name=Bob&age=99&day=Wed" # given example
    # query_string = "?courseId=_172114_1&view=content" # from LJCU lecture site
    query_string = "?page=1&sort=popular&customizable=1&is_featured=1"  # from Thingiverse

    pairs = extract_pairs(query_string)

    print(pairs)


def extract_pairs(query_string):
    if query_string.startswith("?"):
        query_string = query_string[1:]
    parts = query_string.split("&")
    pairs = []
    for part in parts:
        label, info = part.split("=")
        if info.isdigit():
            info = int(info)
        pairs.append((label, info))
    return pairs


main()
