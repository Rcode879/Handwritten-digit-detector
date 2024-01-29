# import necessary packages
import tkinter as tk # GUI package
from tkinter import filedialog # Open files in gui
import cv2 # opencv to convert image to greyscale
from sklearn.metrics import accuracy_score # package to find accuracy of model
from sklearn.neighbors import KNeighborsClassifier # knearest model
import csv # package to read csv files efficiently

# set up labels and data arrays
train_labels = []
train_data = []
test_labels = []
test_data = []

# define our files as variables
training = "mnist_train.csv"
testing = "mnist_test.csv"

def load_data(train_file, test_file):
    data_train = open(train_file, "r") # open file in read mode

    #load training data labels
    for col in data_train:
        train_labels.append(col[0]) # the first column represents the labels

    data_train.close # close file so we can open it again but with the csv module instead

    # load testing data labels:
    # Open file using csv package
    with open(train_file) as file_obj:
        # Create reader object by passing the file
        # object to reader method
        reader_obj = csv.reader(file_obj)

        # Iterate over each row in the csv
        # file using reader object
        for row in reader_obj:
            train_data.append(row)

    for i in range(0, 60000): # range up to 60000 because we have 59999 rows of data
        del train_data[i][0]
        # covert all data to integers
        for x in range(0, 784): # in range of 784 because there is 783 coloumns
            train_data[i][x] = int(train_data[i][x]) # convert to integer

    # Repeating steps above but for testing data:
    data_test = open(test_file, "r")  # open file in read mode

    # load training data labels
    for col in data_test:
        test_labels.append(col[0])  # the first column represents the labels

    data_test.close  # close file so we can open it again but with the csv module instead

    # load testing data labels:
    # Open file using csv package
    with open(test_file) as file_obj:
        # Create reader object by passing the file
        # object to reader method
        reader_obj = csv.reader(file_obj)

        # Iterate over each row in the csv
        # file using reader object
        for row in reader_obj:
            test_data.append(row)

    for i in range(0, 10000):  # range up to 10001 because we have 10000 rows of data
        del test_data[i][0]
        # covert all data to integers
        for x in range(0, 784):  # in range of 784 because there is 783 coloumns
            test_data[i][x] = int(test_data[i][x])  # convert to integer
    print("DATA LOADED") # debug print statement to troubleshoot


load_data(training, testing)



# Create gui:
# create root window
root = tk.Tk()

image_location = [] # list to store the location of exported image



# root window title and dimension
root.title("Number recognition")

# Set geometry (width x height)
root.geometry('4000x2200')

# resize background

# Add image file
bg = tk.PhotoImage(file = 'gui.png')




# Show background image using label
label1 = tk.Label( root, image = bg)
label1.place(x = 0, y = 0)

# Add label
lbl = tk.Label(root, text = "This program will recognise 28 x 28 hand written digits", fg='red', font=("Helvetica", 16), bg='light blue')
lbl.pack()

# Add label
explainlbl = tk.Label(root, text = "WARNING The model accuracy will take a long time to return an output", fg='black', font=("Helvetica", 16), bg='light blue')
explainlbl.pack()

# Create a label widget to display the output
output_label = tk.Label(root, text="Output goes here", font=("Helvetica", 16), bg='light blue')
# pack widget
output_label.pack()


# recognise image and predict
def open_image():

    filename = filedialog.askopenfilename(initialdir="/",title="Select a File", filetypes = (("image files", "*.png"),)) #allow user to only export image files
    filetypes = ("images", "*.png") #allow user to only find png files
    image_location.append(filename)
    print(image_location)
    # If user presses red cross on file explorer pop up:
    for i in range(len(image_location)):
        if image_location[i] == '':
            output_label.config(text="NO IMAGE EXPORTED, TRY AGAIN")
            image_location.clear()
            return

    # confirm on gui that the image has been successfully exported
    output_label.config(text="Image exported")

def find_accuracy():

    clf = KNeighborsClassifier(1)
    clf.fit(train_data, train_labels) #fit training data to model
    pred = clf.predict(test_data)
    acc = accuracy_score(test_labels, pred)*100,"%" #recieve percentage accuracy
    accuracy_line = "Accuracy:", acc

    output_label.config(text=accuracy_line)

def predict():
    #recgonise image
    number_data = []
    img = cv2.imread(image_location[0], cv2.IMREAD_GRAYSCALE)


    # resize image to match MNIST dataset size

    img = cv2.resize(img, (28, 28))



    # flatten array
    img = img.flatten()
    number_data.append(img)

    clf = KNeighborsClassifier(1)

    # predict number
    clf.fit(train_data, train_labels) #fit data to training model
    prediction = clf.predict(number_data)
    prediction_line = "I think this is a ", prediction
    output_label.config(text=prediction_line) #output the prediction on the gui window
    image_location.clear() #clear any previous file location left in the image location list


# Buttons:

# button to find accuracy
accuracy_btn = tk.Button(root, text = "model accuracy" ,fg = "red", height=10, width= 30, font=("Helvetica", 16), command= find_accuracy, bg='light blue' )
accuracy_btn.pack()

# button to export file
export_btn = tk.Button(root, text = "export image" ,fg = "green", command= open_image, height=10, width= 30, font=("Helvetica", 16), bg='light blue')
export_btn.pack()

# button to predict file
predict_btn = tk.Button(root, text = "predict" ,fg = "green", command= predict, height=10, width= 30, font=("Helvetica", 16), bg='light blue')
predict_btn.pack()

# Execute Tkinter
root.mainloop()

