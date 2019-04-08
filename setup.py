from setuptools import setup, find_packages

setup(
    name='window-tiler',
    version='0.0.1',
    python_requires='>=3.6.7',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'window-tiler = window_tiler.window_tiler:move_window',
        ],
    },
)
