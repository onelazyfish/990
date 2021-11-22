from setuptools import setup

setup(name="simplelayout-github-onelazyfish", version="1.0.0",
      description="This is the assignment of IDRL",
      packages=["simplelayout", "simplelayout.generator", "simplelayout.cli"],
      author="onelazyfish", author_email="326042208@qq.com",
      url="https://github.com/onelazyfish", license="MIT",
      install_requires=["numpy", "matplotlib", "scipy"], entry_points={
        "console_scripts": ["simplelayout=simplelayout.__main__:main"],
    })
