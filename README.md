# Beating the Google Chrome Dinosaur Game

# Script 1: `play.py`

This Python script utilizes the OpenCV, NumPy, and PyAutoGUI libraries to capture a region of the screen, count the number of black and white pixels in that region, and perform keyboard actions based on pixel count thresholds. It is primarily designed to automate actions in response to changes in the screen's pixel content.

1. The script will continuously capture a region of the screen defined by its coordinates (left, top, width, and height) and analyze the pixel content within that region.

2. It counts the number of black and white pixels in the captured image.

3. Based on the pixel count thresholds, it presses the 'up' arrow key using PyAutoGUI to simulate a keyboard action.

4. The captured region and pixel counts are displayed in a window using OpenCV.

5. To exit the script, press the 'q' key when the OpenCV window is in focus.

## Dependencies
- OpenCV
- NumPy
- PyAutoGUI

# Script 2: `play_v2.py`

1. This Python script is designed to automate playing the popular T-Rex (Dino) game in a web browser. It uses screen capture, pixel analysis, and keyboard simulation to control the T-Rex character and help it jump over obstacles.

2. Open a web browser and navigate to the T-Rex (Dino) game. Make sure the game is loaded and ready to play.

3. Once the game is running, press 'Q' at any time to exit the script.

4. The script will continuously capture a region of the screen (defined by the top, left, width, and height variables) and analyze the pixel content within that region to detect obstacles.

5. It will simulate pressing the space bar (' ') to make the T-Rex jump when an obstacle is detected. The script also simulates the acceleration of the T-Rex by increasing the search width over time.

6. The x_start, x_end, and y_search_cactus variables control the region where the script searches for obstacles. You can customize these values to match the game's layout and speed.

# Dependencies
- PyAutoGUI
- Keyboard
- OpenCV
- NumPy

# References:
- https://www.youtube.com/watch?v=uNLcYEXsVXQ
- https://www.youtube.com/watch?v=UBLLtJG3lLw