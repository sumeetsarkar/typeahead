def checkifstring(string):
    failchecks = [
        string is None,
        isinstance(string, str) is False,
    ]
    if any(failchecks) or string.strip() == '':
        return False
    return True
