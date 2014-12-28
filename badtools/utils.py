import os


def getIconPath(name="default"):
    # TODO:Documentation for getIconPath()
    icons = os.getenv("BD_ICONS", False)

    if not icons:
        print "getIconPath(): can't get badtools icons "
        return ""

    path = os.path.join(icons, name + ".png")

    if not os.path.exists(path):
        path = os.path.join(icons, "default" + ".png")

    return path
