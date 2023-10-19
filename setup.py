from setuptools import setup

setup(
    name="notification",
    version="0.1",
    packages=["notification"],
    install_requires=[
        "certifi",
        "charset-normalizer",
        "idna",
        "requests",
        "secure-smtplib",
        "urllib3",
    ],
    entry_points={
        "console_scripts": [
            "send_email=notification.send_email:main",
        ],
    },
)
