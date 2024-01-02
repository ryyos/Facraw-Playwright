
def vname(name: str) -> str:
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '+', '=', '&', '%', '@', '#', '$', '^', '[', ']', '{', '}', '`', '~']
    falid = ''.join(char if char not in invalid_chars else '' for char in name)
    
    return falid.replace(" ", "_")