from setuptools import setup, find_packages

setup(
    name='booking-bots',
    version='0.1.1',
    description='A Selenium-based bot for automating booking tasks',
    author='PandaRius',
    author_email='pjm.darius@g',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'selenium',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'booking-bot=booking_bot.bot:run_bot'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
