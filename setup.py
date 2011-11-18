from setuptools import setup, find_packages

version = "0.1"

setup(name="cookieapp",
      version=version,
      packages=find_packages(exclude=['selenium']),

      author='Scott Wilson',
      author_email='scott@idealist.org',

      entry_points={
          'console_scripts': [
            'runapp=cookieapp:run',
            ],
          },

      install_requires=[
        'Werkzeug == 0.8.1',
        'selenium',
        ],

      )
