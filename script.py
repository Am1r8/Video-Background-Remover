print(""""\n\n
 _______  _______  _______  ___   _  _______  ______    _______  __   __  __    _  ______     ______    _______  __   __  _______  __   __  _______  ______   
|  _    ||   _   ||       ||   | | ||       ||    _ |  |       ||  | |  ||  |  | ||      |   |    _ |  |       ||  |_|  ||       ||  | |  ||       ||    _ |  
| |_|   ||  |_|  ||       ||   |_| ||    ___||   | ||  |   _   ||  | |  ||   |_| ||  _    |  |   | ||  |    ___||       ||   _   ||  |_|  ||    ___||   | ||  
|       ||       ||       ||      _||   | __ |   |_||_ |  | |  ||  |_|  ||       || | |   |  |   |_||_ |   |___ |       ||  | |  ||       ||   |___ |   |_||_ 
|  _   | |       ||      _||     |_ |   ||  ||    __  ||  |_|  ||       ||  _    || |_|   |  |    __  ||    ___||       ||  |_|  ||       ||    ___||    __  |
| |_|   ||   _   ||     |_ |    _  ||   |_| ||   |  | ||       ||       || | |   ||       |  |   |  | ||   |___ | ||_|| ||       | |     | |   |___ |   |  | |
|_______||__| |__||_______||___| |_||_______||___|  |_||_______||_______||_|  |__||______|   |___|  |_||_______||_|   |_||_______|  |___|  |_______||___|  |_|

\n\n\n\n""")



print("Importing Modules ...\n")
from skimage.filters import gaussian
from moviepy.editor import VideoFileClip
import mediapipe
import random


vid = input("Enter the Name of Video With the extension.\n\n")

video_clip = VideoFileClip(vid)


print("\nProcessing The Video ...\n\n")
selfie_segmentation =  mediapipe.solutions.selfie_segmentation.SelfieSegmentation(model_selection=1)

def blur_background(im):
    mask = selfie_segmentation.process(im).segmentation_mask[:, :, None]
    mask = mask > 0.8

    bg = gaussian(im.astype(float), sigma=4)
    return mask * im + (1 - mask) * bg



video_clip = video_clip.subclip(0, video_clip.duration)
video_clip = video_clip.fl_image( blur_background )

rando = str(random.randint(0,100))
name = "edited" + rando + ".mp4"
video_clip.write_videofile(name, audio=False)