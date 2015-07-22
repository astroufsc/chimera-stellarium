from distutils.core import setup

setup(
    name='chimera-stellarium',
    version='0.0.1',
    packages=['chimera_stellarium', 'chimera_stellarium.controllers'],
    scripts=[],
    url='http://github.com/astroufsc/chimera-stellarium',
    license='GPL v2',
    author='William Schoenell',
    author_email='william@iaa.es',
    description='Chimera controller plugin for Stellarium integration'
)
