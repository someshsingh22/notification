from setuptools import setup

setup(
    name="notification",
    version="0.1",
    packages=["notification"],
    install_requires=[
        "yagmail==0.14.260",
    ],
    entry_points={
        "console_scripts": [
            "send_email=notification.send_email:main",
        ],
    },
)
