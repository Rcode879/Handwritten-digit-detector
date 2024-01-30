# Handwritten-digit-detector
A python program that trains a Knearest neighbours model on the MNIST data set(which is in the form of a CSV file) to recognise handwritten digits.
Implemented into a TKinter GUI which had a button to train the model, a button to load in your own png file with a handwritten digit and a button to output the model accuracy.

##Required packages: 
CSV, Tkinter, OpenCV, Scikit.learn

##Warning:
- line 16 with variable named "mnist_train.csv", is the csv file file containing the mnist data set to train the model, the file was too large to upload to the repository
- line 96 is the background image of the gui - "gui.png" - you can add your own peronal image by downloading one of your choice and renaming it
- If you wish to test your own image(png), it must be 28 by 28 pixels with a black background and the number written in white
- This model is NOT the most accurate and would most likely be more accurate in a neural network so do not expect perfect predicitons
