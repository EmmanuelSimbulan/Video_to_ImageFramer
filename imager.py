import cv2
import os

def extract_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    
    # Variables for frame extraction
    frame_count = 0
    success = True

    # Read frames until there are no more
    while success:
        success, image = video_capture.read()
        
        if success:
            frame_count += 1
            # Save frame as JPEG image
            frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpeg")
            cv2.imwrite(frame_path, image)
            print(f"Frame {frame_count} saved as {frame_path}")

    # Release the video capture object and close windows
    video_capture.release()
    cv2.destroyAllWindows()

# Replace 'input.mov' with your .mov file path and 'output_frames_folder' with your desired output folder
video_file = 'video path'
output_frames_folder = 'folder path'
extract_frames(video_file, output_frames_folder)
