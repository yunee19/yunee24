import cv2

class VideoRecorder:
    def __init__(self):
        self.preview_mode = True
        self.record_mode = False
        self.recording = False
        self.rtsp_url = "rtsp://210.99.70.120:1935/live/cctv001.stream"
        self.cap = cv2.VideoCapture(self.rtsp_url)
        self.out = None
        self.preview_window = "Preview"
        self.fps = 20.0  # FPS mặc định

    def start_recording(self):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.out = cv2.VideoWriter('VideoRecoder.avi', fourcc, self.fps, (frame_width, frame_height))

    def stop_recording(self):
        self.out.release()

    def toggle_mode(self):
        self.preview_mode = not self.preview_mode
        self.record_mode = not self.record_mode

    def set_fps(self, fps):
        self.fps = fps

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            if self.preview_mode:
                cv2.imshow(self.preview_window, frame)
                key = cv2.waitKey(1)
                if key == 27:  # Phím ESC để thoát
                    break
                elif key == ord(' '):  # Phím Space để chuyển đổi chế độ
                    self.toggle_mode()
            elif self.record_mode:
                if not self.recording:
                    self.start_recording()
                    self.recording = True
                self.out.write(frame)
                cv2.circle(frame, (50, 50), 20, (0, 0, 255), -1)  # Vẽ hình tròn màu đỏ để chỉ ra đang ghi
                cv2.imshow(self.preview_window, frame)
                key = cv2.waitKey(1)
                if key == 27:  # Phím ESC để thoát
                    self.stop_recording()
                    self.recording = False
                    self.toggle_mode()
                elif key == ord(' '):  # Phím Space để chuyển đổi chế độ
                    self.stop_recording()
                    self.recording = False
                    self.toggle_mode()

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    recorder = VideoRecorder()
    recorder.set_fps(30.0)  # Đặt FPS thành 30
    recorder.run()
