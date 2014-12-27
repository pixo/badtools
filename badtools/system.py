import itertools
import re
import os


def extractNumber(name):
    # TODO: Documentation extractNumber()
    try:
        sp = name.split(".")[1]

    except IndexError:
        sp = name

    result = re.findall(r"\d+", sp)

    if len(result) > 0:
        return result[0]
    else:
        return "0"


def lsSeq(path, recursive=True):
    # TODO: Documentation lsSeq()
    # Collapse Group functions
    def collapseGroup(group, root=os.sep):

        if len(group) == 1:
            result = os.path.basename(group[0][1])
            return result

        if root[-1] != os.sep:
            root = root + os.sep

        part = group[0][1].split(".")
        first = extractNumber(group[0][1])
        last = extractNumber(group[-1][1])
        length = len(str(int(last)))
        prefix = re.findall(r"\d+.\w+$", group[0][1])[0]
        ext = part[-1]
        base = group[0][1].replace(part[1], "####")
        base = base.split(root)[-1]

        result = "%s[%s-%s]" % (base, first[-length:], last[-length:])
        return result

    itemDict = dict()
    resultDict = dict()

    if recursive:
        for root, subFolders, files in os.walk(path):
            files.sort()

            for fil in files:
                fullpath = os.path.join(root, fil)
                base = fullpath.split(".")[0].replace(path + os.sep, "")

                if not (base in itemDict):
                    itemDict[base] = list()

                itemDict[base].append(fullpath)

    else:
        files = sorted(os.listdir(path))

        for fil in files:
            fullpath = os.path.join(path, fil)

            if os.path.isfile(fullpath):
                base = fil.split(".")[0]

                if not (base in itemDict):
                    itemDict[base] = list()
                itemDict[base].append(fullpath)

    for key in itemDict:
        groups = [collapseGroup(tuple(group), path)
                  for i, group in itertools.groupby(enumerate(itemDict[key]),
                                                    lambda index_name:index_name[0] - int(extractNumber(index_name[1])))]
        resultDict['\n'.join(map(str, groups))] = itemDict[key]

    return resultDict


def rsync(source="", destination="", excludes=list()):
    # TODO: Documentation
    """ rsync in python """

    """ Basic update args """
    update = "--progress -rvuh --ignore-existing"

    """ Excludes args """
    exclude = ""
    for i in excludes:
        if isinstance(i, str):
            exclude += "--exclude=%s " % i

    exclude = exclude.rstrip()

    """ Creating rsync command """
    cmd = "rsync %s %s %s %s" % (update, exclude, source, destination)
    os.system(cmd)

    return cmd