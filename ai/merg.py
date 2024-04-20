import cv2
from gtts import gTTS
import os

def speak_in_hindi(text):
    tts = gTTS(text=text, lang='hi')
    tts.save('output.mp3')
    os.system('output.mp3')  # You can use any media player that supports MP3

file_location = 'F:/new folder/newsai/ai.txt'  # Replace with the location of your text file

# Read the content of the file
with open(file_location, 'r', encoding='utf-8') as file:
    content = file.read()


speak_in_hindi(content)

# Open the video file
cap = cv2.VideoCapture('F:/new folder/newsai/aivid2.mp4')

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file")
    exit()

# Get the frame dimensions (height and width) of the video
frame_width = int(cap.get(1))  # Get the width of the frame
frame_height = int(cap.get(2))  # Get the height of the frame
print(f"Video Frame Size: {frame_width}x{frame_height}")

while True:
    # Read frames from the video
    ret, frame = cap.read()

    # Check if the video has ended
    if not ret:
        # If the video has ended, rewind it
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Display the frame
    cv2.imshow('Frame', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Release the video file and close the window
cap.release()
cv2.destroyAllWindows()
