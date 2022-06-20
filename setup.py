from setuptools import setup,find_packages

def readme():
    with open('README.rst') as f:
        return f.read()
    
setup(name='barnaba',
      description='analyze nucleic acid 3D structures and MD trajectories',
      long_description=readme(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
      ],      
      url='https://github.com/srnas/barnaba',
      author='Sandro Bottaro',
      author_email='sandro.bottaro@gmail.com',
      use_scm_version = True,
      setup_requires = ['setuptools_scm','setuptools_scm_git_archive'],
      packages=find_packages(),
      python_requires='>=2.6',
      install_requires=['numpy','scipy','mdtraj','future','sklearn'],
      scripts=['bin/barnaba'],
      zip_safe=False)


