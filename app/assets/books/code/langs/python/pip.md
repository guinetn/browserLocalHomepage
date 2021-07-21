# PIP 

Python package is a module that can contain other modules or recursively, other packages. Pip is one of the widely used package management system to install and manage software packages written in Python and found in Python Package Index (PyPI).

default, standard package-management system on Python >= 3.4  
Packages that are managed by pip are built using [Setuptools](https://pypi.org/project/setuptools/)
a package-development-process library to facilitate packaging Python projects (GitHub Python projects have a `setup.py` at the root of the project 

pip packages are usually hosted on a PyPI. This can be a private or public repository for open-source or private Python packages. For those not familiar with the Python package repository, when you think of PyPI, think of RubyGems for Ruby, Packagist for PHP, Maven for Java, CPAN for Perl, and npm for Node.js.

## virtualenv
http://www.virtualenv.org/
pip has limitations, such as lack of package isolation. This means out of the box, you can’t run multiple Python versions in an isolated manner. This is where virtualenv solves this very specific problem by allowing multiple Python projects that have different (and often conflicting) requirements to coexist on the same computer.


# PIP COMMANDS
pip --version
python -m pip install --upgrade pip
pip install 'flask==1.1.2'
pip install -r requirements.txt

July 2020: 235 000 Python packages 

# PyPI - Python Package Index

https://pypi.org/
Repository of software for the Python programming language. This repository houses the packages created and shared
You can install any package from Pypi using pip which is the package installer for Python.
See also I:\code_langs\python\@python\virtualenv.py



  install                     Install packages
   pip install -r requirements.txt     install all the packages mentioned in the requirements.txt fil

  requirements.txt
  tensorflow==2.2.0
  numpy==1.19.1

    --requirement <file>/ -r   for installing from the given requirements file. A requirements file is a list of all of a project’s dependencies. This text file contains all the package required including the specific version of each dependency. 

  download                    Download packages.
  uninstall                   Uninstall packages.
                              pip uninstall pandas
    few exceptions that cannot be uninstalled. They are:
      Pure distutils packages installed with python setup.py install, and
      Script wrappers installed by python setup.py develop.

      pip uninstall --yes pandas
        --requirement <file>/ -r for uninstalling packages from the requirements file.
        --yes / -y . This option if selected doesn’t ask for confirmation during uninstalling a package.


  freeze                      Output installed packages in requirements format.
      pip freeze > requirments.txt
      cat requirments.txt

  list                        List installed packages.
    pip list --outdated       listing all the outdated packages 
    pip list -o
    
    pip list --uptodate       listing all the up-to-date packages
    pip list -u
    
    pip list --format json    output format: columns (default), freeze, JSON

  show                        Show information about installed packages.                              
                                >pip show pandas
                                >pip show --verbose pandas            complete details
                                >pip show graphviz
                                  Name: graphviz
                                  Version: 0.13.2
                                  Summary: Simple Python interface for Graphviz
                                  Home-page: https://github.com/xflr6/graphviz
                                  Author: Sebastian Bank                                                            
                                  Location: c:\users\nguin\anaconda3\lib\site-packages
                                  Requires:
                                  Required-by: diagrams
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
                              >pip version: pip 20.1.1 from C:\Users\nguin\anaconda3\lib\site-packages\pip (python 3.8)
                              >sys.version: 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)]
                              >sys.executable: C:\Users\nguin\anaconda3\python.exe
  help                        Show help for commands.
  pip help <install>

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to
                              WARNING, ERROR, and CRITICAL logging levels).

 

PATH
  C:\Users\nguin\anaconda3\lib\site-packages

pip install <package_name>
pip install "SomeProject==1.4"
pip install "SomeProject>=1,<2"   To install greater than or equal to one version and less than another:
pip install "SomeProject~=1.4.2"  To install a version that’s “compatible” with a certain version: 4

pip install -r requirements.txt
requirements.txt
	astroid==2.0.4
	atomicwrites==1.1.5
	attrs==18.1.0
	...

https://packaging.python.org/tutorials/installing-packages/
https://pypi.org/
PyPI - the Python Package Index. 127,213 Projects
a repository of software for the Python programming language.
ex: pip install sewer


### Source Distribution (or “sdist”)
	
A distribution format (usually generated using python setup.py sdist) that provides metadata and the essential source files needed for installing by a tool like pip, or for generating a Built Distribution.

### Wheel

a built-package format for Python
a ZIP-format archive with a specially formatted file name and the .whl extension
A Built Distribution format introduced by PEP 427, which is intended to replace 
the Egg format. Wheel is currently supported by pip