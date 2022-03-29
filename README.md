# ML-Cohort-

## Task 1
- Kaggle dataset https://www.kaggle.com/mbkinaci/fruit-images-for-object-detection
- A function in the jupyter notebook do the following tasks:
     -  Input:
           -  Takes the path of the folder as the input
     - Process:
          -  Loads all the images and convert them to an array
          -  Convert all the images to grayscale images
     - Output:
          -  Number of images
          -  Format type of the images
          -  Saving all the grayscale images to another folder
- Example
Input 
![apple_1](https://user-images.githubusercontent.com/67424390/160527142-c6e3bd3a-d4fb-45bb-9ab8-efa03f049d77.jpg)
Output 
![apple_1](https://user-images.githubusercontent.com/67424390/160527222-b60c61a7-b183-4a10-b708-97cfe047f109.jpg)

## Task 2 
1. Data https://drive.google.com/drive/folders/1KZ5sVLpEMqt4I4Yj3Sg8BAVJQ-5h9Nyw?usp=sharing 
2. A function in python script do the following: 
  i. Inputs: Input the folder name and csv filename through command line
  ii. To-Do:
    1. Read all the images
    2. Read the csv file, and get the image label names and coordinates
    3. Draws the bounding boxes for every image, using the corresponding image’s coordinates (Use different colour and thickness for the bounding boxes)
    4. Added labels for every image (Use different font, font colour, font, size)
    5. Created another folder and saved all the images to the folder
3. Example
- Input  ![cats_000](https://user-images.githubusercontent.com/67424390/160527776-58b5c446-2800-4fec-b7cf-6f1a36fa6867.jpg) 
- Output ![cats_000 jpg](https://user-images.githubusercontent.com/67424390/160527798-99dfcb74-1e85-4033-897e-c52aa3c69d63.jpg)

## Task 3 
AIM: To create a neural network model of the highest accuracy, with the least number of parameters
(can read about parameters - https://towardsdatascience.com/model-parameters-and-hyperparameters-in-machine-learning-what-is-the-difference-702d30970f6 )
1. Download the dataset - https://drive.google.com/drive/folders/1AlztDRzHhuavHPb77o9ZDHGIp6za77AR?usp=sharing
2. Created all the pre-processing steps similar to the one from the above notebooks
3. Created a Neural network model using Keras and train the model on the training
dataset
4. Tested the model on the test dataset

### Model architecture
![image](https://user-images.githubusercontent.com/67424390/160528540-c4159d52-177e-45af-8377-c1b47a8f87b2.png)

### Model Accuracy
![image](https://user-images.githubusercontent.com/67424390/160528755-5a8ad289-f5ba-41ed-a1aa-9c2d6baece35.png)
