from setuptools import setup

setup(
    name='notification',
    version='0.1',
    packages=['notification'],
    install_requires=[
        'certifi==2021.5.30',
        'charset-normalizer==2.0.10',
        'idna==3.3',
        'requests==2.26.0',
        'smtplib==0.0.1',
        'urllib3==1.26.6',
    ],
    entry_points={
        'console_scripts': [
            'send_email_gmail=notification.send_email_gmail:main',
        ],
    },
)
