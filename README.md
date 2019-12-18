# Data_Mining


This repository consists of my projects, which I did in my Data Mining class. Text Search, Image caption generation and search and Text Classifier.

There are 3 phases in this project.

Required Libraries Download following libraries:

1. pip install flask
2. pip install numpy
3. pip install nltk
4. pip install scipy
5. pip install sklearn
6. pip install Flask-Images
7. pip install image
8. pip --default-timeout=60 install "tensorflow-gpu>=1.19,<2"


Steps to run and deploy in localhost

1. Install flask in your environment.
2. Download this repo to a folder
3. Navigate upto the 'app' directory
4. from a console run the app.py file by the command python app.py
5. Hit localhost:5000 in browser.

All the experiments, challenges I faced along with the steps to do this project are in my blog.
You can check that out here:
https://yashdani.school.blog/


Example for Text Search:-

**"Bad Man"**

**Result:-**

Title: The 50 Worst Movies Ever Made
Overview: There are some movies that are so bad they're good. And there are some movies that are so bad- that they're just bad...
Release Date: 2004-07-13
Idf Score of ('bad', 0.6210325561848423):
TF Score of ('bad', 0.6210325561848423):
TF-IDF Score of ('bad', 0.6210325561848423):
Idf Score of ('man', 0.0):
TF Score of ('man', 0.0):
TF-IDF Score of ('man', 0.0):
Tf-idf Score: 0.29859921085493146


Title: Bad Boy
Overview: A lawman tries to find the source of a juvenile delinquent's bad behavior.
Release Date: 1949-02-22
Idf Score of ('bad', 0.6135383405132174):
TF Score of ('bad', 0.6135383405132174):
TF-IDF Score of ('bad', 0.6135383405132174):
Idf Score of ('man', 0.0):
TF Score of ('man', 0.0):
TF-IDF Score of ('man', 0.0):
Tf-idf Score: 0.2949959104107953


Title: Bad Night
Overview: When Kate and Abby are mistaken for famous art thieves, their fun night out quickly goes from good to bad.
Release Date: 2015-07-21
Idf Score of ('bad', 0.5849109620832785):
TF Score of ('bad', 0.5849109620832785):
TF-IDF Score of ('bad', 0.5849109620832785):
Idf Score of ('man', 0.0):
TF Score of ('man', 0.0):
TF-IDF Score of ('man', 0.0):
Tf-idf Score: 0.28123155534938205
