from setuptools import setup, find_packages


setuptools.setup(
     name='kaggle_stackoverflow_survey',
     version='0.0.1',
     scripts=[''],
     author="Pavan Burra",
     author_email="pavank.burra@gmail.com",
     description="Contains function to analyse the SO survey data from Kaggle",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="",
     packages=find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )