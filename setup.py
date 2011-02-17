from distutils.core import setup
import os

from adb import get_version

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('adb'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[13:] # Strip "adb/" or "adb\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(name='python-adb',
      version=get_version().replace(' ', '-'),
      description='A python wrapper around the Android Debug Bridge',
      author='Ryan Brady',
      author_email='ryan@ryanbrady.org',
      package_dir={'adb': 'adb'},
      packages=packages,
      url="https://github.com/rbrady/python-adb",
      long_description=read("README"),
      package_data={'adb': data_files},
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      )
