# cut_pic
Cutout picture into a square for image machine learning

# necessary library
os\
cv2\
numpy

# Usage
1. Put images in "input_pic" folder.
2. Run "cut_put.py" file.
3. Some images in "input_pic" folder are displayed.
   if there in the obfject of interest in displayed picture,
   you click start and end for a square and input any key.
   if not, you only input any key.\
   <img src="https://github.com/konishi0125/cut_pic/blob/main/readme_picture/bird.jpg" width="320px">
   <img src="https://github.com/konishi0125/cut_pic/blob/main/readme_picture/not_bird.jpg" width="320px">
4. Two files "ok.txt" and "ng.txt" are made in "result" folder.\
   ok.txt:picture name and cutout coordinates\
   picture_name start_x start_y end_x end_y\
   ng.txt:picture name:
   picture_name