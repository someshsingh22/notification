from setuptools import setup

setup(
    name='notification',
    version='0.1',
    packages=['notification'],
    install_requires=[
        'certifi',
        'charset-normalizer',
        'idna',
        'requests',
        'smtplib',
        'urllib3',
    ],
    entry_points={
        'console_scripts': [
            'send_email_gmail=notification.send_email_gmail:main',
        ],
    },
)
