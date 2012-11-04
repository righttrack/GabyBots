
def target_name_count(target, text):
    """
    Count the number of times each target name of a given target appears in the given text.
    @param target: The target to search for
    @param text: The text to search in
    @return: A list of (target name, occurrences) tuples
    """
    for line in text:
        for name in target.names:
            if name in line:
                pass
    # you should end up with some list of tuples of (target_name, count) that looks like
    return [('barack', 2), ('obama', 1)]
