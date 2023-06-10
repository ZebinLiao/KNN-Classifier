# KNN-Classifier
A simple KNN Classifier for deciding the next move for pacman, given a set of good moves.

To run this code, executet he command: 

python pacman.py --pacman ClassifierAgent

The code written for this project is all in classifier.py

To summarise:

  - Good-moves.txt contains past states that pacman has been in and their corresponding good moves that pacman should execute.
  - This data is used to fit and predict move for the pacman using a KNN algorithm (not using scikit).

More detailed documentation is in the file classifier.py
