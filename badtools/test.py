import badass.core as core


def pub():
    path = "/badass/users/pixo/projects/prj/chr/mickey/mod/a/aa.ma"
    core.push(doc_id="prj_chr_mickey_mod_a", path=path, comment="unit test")


def release():
    core.release(doc_id="prj_chr_mickey_mod_a", version=122)


if __name__ == '__main__':
    # pub()
    release()
