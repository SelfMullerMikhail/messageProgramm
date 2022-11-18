def get_way(file_, step):
    a = (file_.split("\\"))
    del a[-step:]
    a = "\\".join(a)
    return a