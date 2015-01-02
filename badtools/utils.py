import os
import badass.utils


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


def createProjectBoot(name=False, serveradress=False, site_root="/badass",
                      sync_root=False):
    """
    This function create a project environment file.
    It contains project environment variables related to the project.
    This file is sourced each times a user log a project via the bd-project.

    :param name: The project name.
    :type name: str
    :param serveradress: The db server ip adress
    :type serveradress: str
    :param syncroot: The adress of the directory to sync
    :type syncroot: str
    :returns:  str/bool -- If created return the file path else False

    **Example:**

    >>> createProjectBoot(name="prod", serveradress="127.0.0.1",
    >>>                  sync_root="192.168.0.24:/volume1")
    >>> '/badass/projects/prod/boot/environment.sh'
    >>> '/badass/projects/prod/boot/toolchain.sh'
    """

    if not name or not serveradress or not site_root or not sync_root:
        return False

    if site_root[0] is not "/":
        site_root = "/" + site_root

    # default toolchain definition
    toolchain = "declare -a ToolChain=(\n"
    toolchain += "'badtools'\n"
    toolchain += "'badpack'\n"
    toolchain += ")\n"

    # default environment definition
    env = "export BD_PROJECT=%s\n" % name
    env += "export BD_ROOT=%s\n" % site_root
    env += "export BD_HOME=$BD_ROOT/users/$USER\n"
    env += "export BD_REPO=$BD_ROOT/projects\n"
    env += "export BD_USER_REPO=$BD_HOME/projects\n"
    env += "export BD_SHARE=$BD_ROOT/softs\n"
    env += "export BD_SYNCROOT=%s\n" % sync_root    # TODO: Fixe adress
    env += "export BD_DBADRESS=badass:badass@%s\n" % serveradress

    # get toolchain and environment path
    boot_dir = os.path.join(site_root, 'projects', name, 'boot')
    env_file = os.path.join(boot_dir, "environment.sh")
    toolchain_file = os.path.join(boot_dir, "toolchain.sh")

    # create toolchain and environment file
    badass.utils.createFile(env_file, env)
    badass.utils.createFile(toolchain_file, toolchain)
    os.chmod(env_file, 0o644)
    os.chmod(toolchain_file, 0o644)
