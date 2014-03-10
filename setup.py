from distutils.core import setup

setup(name='bitmath',
      version='0.5.2',
      description='Pythonic module for representing and manipulating file sizes with different prefix notations.',
      maintainer='Tim Bielawa',
      maintainer_email='timbielawa@gmail.com',
      url='https://github.com/tbielawa/bitmath',
      license='MIT',
      package_dir={'bitmath': 'bitmath'},
      packages=['bitmath'],
      classifiers = [
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Software Development :: Libraries',
          'Topic :: System :: Filesystems',
          'Topic :: Utilities'
      ]
)
