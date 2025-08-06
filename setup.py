from distutils.core import setup

from quatrosec.config import Configuration

setup(
    name='Quatrosec',
    version=Configuration.version,
    author='derv82',
    author_email='botanimuhamed@gmail.com',
    url='https://github.com/xbotani/Quatrosec',
    packages=[
        'quatrosec',
        'quatrosec/attack',
        'quatrosec/model',
        'quatrosec/tools',
        'quatrosec/util',
    ],
    data_files=[
        ('share/dict', ['wordlist-top4800-probable.txt'])
    ],
    entry_points={
        'console_scripts': [
            'quatrosec = quatrosec.quatrosec:entry_point'
        ]
    },
    license='GNU GPLv2',
    scripts=['bin/quatrosec'],
    description='Wireless Network Auditor for Linux',
    #long_description=open('README.md').read(),
    long_description='''Wireless Network Auditor for Linux.

    Cracks WEP, WPA, and WPS encrypted networks.

    Depends on Aircrack-ng Suite, Tshark (from Wireshark), and various other external tools.''',
    classifiers = [
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ]
)
