from setuptools import setup, find_packages

with open("requirements.txt") as fp:
    req = fp.read()
setup(
    name="gui_app",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    py_modules=["run", "setup"],
    install_requires=req,
    package_data={'Rapid_Screenshot': [""]},
    entry_points={'console_scripts': ['sel = run:main']

}

)