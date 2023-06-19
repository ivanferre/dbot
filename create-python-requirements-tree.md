# The Python Requirements File and How to Create it

<https://learnpython.com/blog/python-requirements-file/>

    pip freeze > requirements.txt
 
    # make sure all python modules are updated.
    # this is not an optimal solution. see https://stackoverflow.com/questions/2720014/how-to-upgrade-all-python-packages-with-pip
    pip list --outdated | awk 'NR > 2 { print $1 }' | xargs -n1 pip install -U

Drop the first lines of a text file: <https://unix.stackexchange.com/questions/37790/how-do-i-delete-the-first-n-lines-of-an-ascii-file-using-shell-commands>

It is also possible to upgrade everything with `pip install -U -r requirements.txt`.

    pip freeze > requirements.txt

## NOT USING IT: Building the Python Project for Deployment

[How to Package Python Dependencies for Publication](https://www.activestate.com/resources/quick-reads/how-to-package-python-dependencies-for-publication/)

Make sure setuptools package is installed and up-to-date:

    python -m pip install --upgrade pip setuptools
