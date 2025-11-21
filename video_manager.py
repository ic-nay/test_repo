import cv2

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

        ret, frame = self.cap.read()

        if not ret:
            print(f"⚠️ Camera {self.camera_id} failed")
            return [False, "Failed to connect to camera {self.camera_id}"]
        
        return [True, frame]