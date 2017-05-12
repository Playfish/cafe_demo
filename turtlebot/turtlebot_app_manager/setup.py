from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
	packages=['app_manager'],
	package_dir={'':'src'},
    scripts = [ 
                'scripts/app_manager',
                'scripts/appmaster',
                'scripts/rosget',
                'scripts/test_app.py',
              ]
)

setup(**setup_args)
