import os


def getIconPath(name="default"):
    # TODO:Documentation for getIconPath()
    icons = os.path.join(os.getenv("BD_ICONS"))
    path = os.path.join(icons, name + ".png")

    if not os.path.exists(path):
        path = os.path.join(icons, "default" + ".png")

    return path