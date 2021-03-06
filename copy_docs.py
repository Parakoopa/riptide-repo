#!/usr/bin/python3

# Copy the documentation of all riptide entities into the riptide docs
# Workdir is the root of the documentation repo
import glob
import os
import shutil

repo_path = os.path.dirname(os.path.realpath(__file__))
docs_path = os.path.join(os.getcwd(), 'source', 'repo_docs')

# Delete directories
try:
    shutil.rmtree(docs_path)
except FileNotFoundError:
    pass
os.makedirs(docs_path)

# Create info file
with open(os.path.join(docs_path, 'README_CONTRIBUTORS'), 'w') as file:
    file.write("The contents of this directory are auto-generated by https://github.com/Parakoopa/riptide-repo. "
               "DO NOT EDIT.")


def copy_files(type):
    os.makedirs(os.path.join(docs_path, type))
    for file in list(glob.glob(os.path.join(repo_path, type, '*', 'README.rst'))):
        name = file.replace(repo_path + os.path.sep, '').split(os.sep)[1]
        target_name = os.path.join(docs_path, type, '%s.rst' % name)
        print(target_name + "...")

        # Insert the link to the repository before all contents:
        with open(file, 'r') as f:
            lines = [".. AUTO-GENERATED, SEE README_CONTRIBUTORS. DO NOT EDIT.\n\n"] + f.readlines()

        index = 0
        for index, line in enumerate(lines):
            if line.startswith("..  contents::"):
                break

        lines.insert(index, "**Link to entity in repository:** "
                            "`<https://github.com/Parakoopa/riptide-repo/tree/master/%s/%s>`_\n\n" % (type, name))

        with open(target_name, "w") as f:
            f.writelines(lines)


copy_files('app')
copy_files('service')
copy_files('command')
