from setuptools import setup

APP = ['testapp.py']
DATA_FILES = ['semester.txt']
OPTIONS = {
 'iconfile':'icon.icns',
 'argv_emulation': True,
 'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
