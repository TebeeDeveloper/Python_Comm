from setuptools import setup, find_packages

setup(
    name="enigma",
    version="1.0.0",
    author="Tebee_Sunaookami",
    description="Personally Module",
    long_description=open("README.md").read(),
    author_email="tebeebmgo@gmail.com",
    url="https://github.com/TebeeDeveloper/Python_Comm",
    packages=find_packages(),
    install_requires = 'enigma',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        # Chọn phiên bản Python mà cậu hỗ trợ:
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8', # Phiên bản Python tối thiểu
)
