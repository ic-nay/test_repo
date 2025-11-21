import cv2
import time
import datetime
import os

cv2.utils.logging.setLogLevel(cv2.utils.logging.LOG_LEVEL_ERROR)

class StreamWatcher():
    def __init__(self, stream_url, camera_id):
        self.stream_url = stream_url
        self.camera_id = camera_id
        self.cap = cv2.VideoCapture(stream_url)
        

    def capture_frame(self):
        if not self.cap.isOpened():
            print(f"❌ Failed to connect to camera {self.camera_id}")
            return [False, "Failed to connect to camera {self.camera_id}"]

        print(f"📡 Connected to camera {self.camera_id}")

        last_capture_time = time.time()

        ret, frame = self.cap.read()

        if not ret:
            print(f"⚠️ Camera {self.camera_id} failed")
            return [False, "Failed to connect to camera {self.camera_id}"]
        
        return [True, frame]

        current_time = time.time()
        if current_time - last_capture_time >= FRAME_INTERVAL:
            # Timestamp for filename
            timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")
            filename = os.path.join(SAVE_PATH, f"{cameraid}{timestamp}.jpg")

            # Save the frame
            cv2.imwrite(filename, frame)
            print(f"📸 Saved frame: {filename}")

            last_capture_time = current_time