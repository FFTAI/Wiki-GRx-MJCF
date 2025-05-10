from setuptools import find_packages
from distutils.core import setup

setup(
    name="urdf2mjcf",
    version="1.0.0",
    description="Convert URDF to MJCF",
    author="Jason Chen",
    author_email="xin.chen@fftai.com",
    license="Apache-2.0",
    packages=find_packages(),
    package_dir={"": "src"},
    python_requires='>=3.7',
    scripts=[
        "scripts/urdf2mjcf"
    ],
    install_requires=[
        "mujoco>=3.0.0",
        "defusedxml==0.7.1",

        # 文件格式整理
        "lxml",
    ]
)
