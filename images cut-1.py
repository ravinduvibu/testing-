import cv2
import os

# Function to extract frames from video
def extract_frames(video_path, output_folder):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Total number of frames
    duration = total_frames / fps  # Duration in seconds
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through each second
    for second in range(0, int(duration)):
        frame_number = int(second * fps)  # Frame at this second
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)  # Set the frame position
        
        ret, frame = cap.read()
        
        if ret:
            # Save frame as PNG
            output_filename = os.path.join(output_folder, f"frame_{second + 1}.png")
            cv2.imwrite(output_filename, frame)
            print(f"Saved frame {second + 1}")
        else:
            print(f"Could not read frame {second + 1}")
    
    # Release the video capture object
    cap.release()

# Input video file path (updated path with raw string)
video_path = r"C:\Users\Ravindu-PC\Desktop\New folder\input\WhatsApp Video 2024-12-11 at 11.04.48_9ba0084a.mp4"

# Output folder to save PNG frames
output_folder = r"C:\Users\Ravindu-PC\Desktop\New folder\output_frames"

# Extract frames from video
extract_frames(video_path, output_folder)
