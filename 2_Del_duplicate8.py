from configparser import ConfigParser

cfg = ConfigParser()
cfg.read("./0_Settings.ini")
file_address = cfg.get('address', 'file_address_is')


def remove_duplicate():
    array = []
    with open(file_address + "data/1_log8.txt", "r") as files:
        for line in files.read().split("\n"):
            if line != "" and not line.startswith("â€”"):
                duplicate = False
                for item in array:
                    if item == line:
                        duplicate = True
                if not duplicate:
                    array.append(line)
    out_put = "\n".join(array)
    with open(file_address + "data/2_filtered_log8.txt", "w") as file:
        file.write(out_put)


def remove_ready_docs():
    hashfile = open(file_address + "data/2_filtered_log8.txt", "r").readlines()
    exceptionsfile = open(file_address + "data/2_url_uncheck8.txt", "r").readlines()
    result_array = []
    for hash in hashfile:
        exists = False
        for exception in exceptionsfile:
            if hash == exception:
                exists = True
        if not exists:
            result_array.append(hash)
    complite_array = "".join(result_array)
    with open(file_address + "/data/2_url_uncheck8.txt", "w") as uncheck:
        uncheck.write(complite_array)


remove_duplicate()
remove_ready_docs()
