from setuptools import setup, find_packages

setup(
    name='task-booker',
    version='0.1.0',
    description='A Selenium-based bot for automating booking tasks',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'selenium',
        'schedule',
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
