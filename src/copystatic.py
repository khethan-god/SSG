import os
import shutil

# both functions in this file operate recursively

# Now we need to write a function that copies all the contents
# from the source directory, which is `static/` and move it to
# `public/` directory where we will store all the generated
# stuff.

def list_paths(source_path, lst):
    # this function lists all paths in the source
    for filename in os.listdir(source_path):
        file_path = os.path.join(source_path, filename)
        if os.path.isdir(file_path):
            lst.extend(list_paths(file_path, []))
        else:
            lst.append(file_path)
    return lst


def copy_files_recursive(source_dir_path, dest_dir_path):
    # this function copies all contents to the destination
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)
