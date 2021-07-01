# Environnements virtuels

Virtual environments isolate different libraries and versions to keep projects working while having differents versions of libraries
Solve dilemna "Project X depend on version 1.x of this library but projet Y need version 4.x” and kept your global directory  
site-packages clean and maintainable. 
Fix conflicting packages 

- https://medium.com/pankajmathur/what-is-anaconda-and-why-should-i-bother-about-it-4744915bf3e6	

# virtualenv 

CLI tool that needs a Python interpreter to run
Create a folder having specific packages/executables versions for a project

- https://pypi.org/project/virtualenv/
- https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html

1. Install virtualenv
> pip install virtualenv
> virtualenv --help

2. Create a virtual environment
> virtualenv my_venv

## pipx

Install and Run Python Applications in Isolated Environments  
~ macOS's brew, JavaScript's npx, Linux's apt
pip is a general-purpose package installer for both libraries and apps with no environment isolation  
pipx is made specifically for application installation, as it adds isolation yet still makes the apps available in your shell: 
pipx creates an isolated environment for each application and its associated packages, making the command available globally

- https://pypi.org/project/pipx/

python3 -m pip install --user pipx
python3 -m pipx ensurepath
python3 -m pip install --user -U pipx    Upgrade pipx
pipx completions
pipx install PACKAGE   creates a venv, installs the package, adds package's associated applications (entry points...exe) to a location on your PATH. 

pipx install git+https://github.com/psf/black.git
pipx install git+https://github.com/psf/black.git@branch  # branch of your choice
pipx install git+https://github.com/psf/black.git@ce14fa8b497bae2b50ec48b3bd7022573a59cdb1  # git hash
pipx install https://github.com/psf/black/archive/18.9b0.zip  # install a release

pipx run 	downloads and runs Python "apps" in a one-time, temporary environment, leaving your system untouched afterwards.
			to run the latest version of an app but don't necessarily want it installed on your computer.
			Re-running the same app is quick because pipx caches Virtual Environments on a per-app basis. 
			The caches only last a few days, and when they expire, pipx will again use the latest version of the package. This way you can be sure you're always running a new version of the package without having to manually upgrade.

## venv

Python 3.3 has a subset of virtualenv package integrated into the standard library under the venv module.
but venv is slow, not upgrade-able, not extendable...

> md my_project_folder
> cd my_project_folder
> python -m venv my_venv    # Creating virtual environment in Windows
> python3 -m venv my_venv   # Creating virtual environment in Mac/Linux

3. Delete virtual environment
- delete the folder 
- rm -rf my_venv


## virtualenvwrapper

- Commands to easily work with virtual environments: create, delete, copy, switch
- Put all your virtual environments in one place
- https://virtualenvwrapper.readthedocs.io/en/latest/

> pip install virtualenvwrapper
> export WORKON_HOME=~/Envs
> source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv env1
pip install django
lssitepackages
ls $WORKON_HOME
env1            hook.log
(env1)$ mkvirtualenv env2
echo 'cd $VIRTUAL_ENV' >> $WORKON_HOME/postactivate
which sphinx-build
/Users/dhellmann/Envs/env3/bin/sphinx-build


