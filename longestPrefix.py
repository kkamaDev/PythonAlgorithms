def longestPrefix(*str):
    if not str:
        return ""
    prefix = min(str,key=len)
    for word in str:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
        if not prefix:
            return ""
    return prefix
print(longestPrefix('flow', 'flower', 'flight'))
        