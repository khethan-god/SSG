import os
import shutil

from copystatic import copy_files_recursive


dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)


main()


# note: shutil.copytree(src, dst) copies an entire directory tree
# rooted at src to a directory named dst and return the destination
# directory