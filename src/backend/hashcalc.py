from hashlib import md5

def checkromhash(file):
    # Construct an sha256 algorith
    hasher = md5()

    # Read the contents of the file into the hash algorithm
    hasher.update(open(file,'rb').read())

    hash = hasher.hexdigest()

    if hash == "20b854b239203baf6c961b850a4a51a2":
        return "us"
    elif hash == "85d61f5525af708c9f1e84dce6dc10e9":
        return "jp"
    elif hash == "45676429ef6b90e65b517129b700308e":
        return "eu"
    else:
        return False
