from setuptools import setup

APP = ['Grades.py']
OPTIONS = {
 'iconfile':'icon.icns',
 'argv_emulation': True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
