from setuptools import setup

setup(
    name='news',
    version='1.0',
    py_modules=['news'],
    install_requires=[
        'Click','requests', 'pyfiglet'
    ],
    entry_points='''
        [console_scripts]
        news=news:cli
    ''',
)