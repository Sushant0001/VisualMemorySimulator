import os
import cv2
from PyQt5.QtCore import QThread, pyqtSignal

def extract_number(filename):
    """Extracts the numerical part from a filename."""
    number_str = ''.join(filter(str.isdigit, filename))
    return int(number_str) if number_str else 0

class VideoGenerationWorker(QThread):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, image_folder, video_name='output_video.avi'):
        super().__init__()
        self.image_folder = image_folder
        self.video_name = video_name

    def run(self):
        try:
            images = [img for img in os.listdir(self.image_folder) if img.endswith(".png")]
            images.sort(key=extract_number)  # Sort images by name if they have numerical order

            if not images:
                raise ValueError("No PNG images found in the directory.")

            # Read the first image to get the frame size
            first_image_path = os.path.join(self.image_folder, images[0])
            frame = cv2.imread(first_image_path)
            if frame is None:
                raise ValueError(f"Failed to read the image {first_image_path}")
            height, width, layers = frame.shape
            size = (width, height)

            # Create a VideoWriter object with 20 frames per second
            out = cv2.VideoWriter(self.video_name, cv2.VideoWriter_fourcc(*'MJPG'), 20, size)

            try:
                for image in images:
                    img_path = os.path.join(self.image_folder, image)
                    frame = cv2.imread(img_path)
                    if frame is None:
                        print(f"Warning: Skipping unreadable image {img_path}")
                        continue
                    out.write(frame)
            except Exception as e:
                self.error.emit(str(e))
            finally:
                out.release()
            self.finished.emit(self.video_name)
        except Exception as e:
            self.error.emit(str(e))
