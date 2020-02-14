from setuptools import setup


setup(name="tap-customerx",
      version="1.0.5",
      description="Singer.io tap for extracting data from the CustomerX API",
      author="Stitch",
      author_email="dev@stitchdata.com",
      url="http://singer.io",
      classifiers=["Programming Language :: Python :: 3 :: Only"],
      py_modules=["tap_customerx"],
      install_requires=[
          "pendulum==2.0.4",
          "requests==2.21.0",
          "singer-python==5.4.1",
      ],
      entry_points="""
          [console_scripts]
          tap-customerx=tap_customerx.cli:main
      """,
      packages=["tap_customerx",
                "tap_customerx.streams"],
      include_package_data=True,
)
