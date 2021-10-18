from setuptools import setup

setup(
    name = 'sat-pkg-RUDOLF-FANCHINI',
    version = '0.0.1',
    author = 'Rudolf Josef Fanchini',
    author_email = 'fanchinirudolf@gmail.com',
    description = 'A mexican taxes helper',
    long_description = 'file: README.md',
    packages=['src.SAT'],
    install_requires=['tkinter'],
    url= 'https://github.com/fanchiniRudolf/sat',
    license= 'MPL-2.0 License',
)