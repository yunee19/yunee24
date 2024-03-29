#This is a Video Recorder using OpenCV


![img](https://github.com/yunee19/yunee24/assets/133479803/264a4b41-5053-41d5-aa90-d23aa8ca2dc0)


[[![Video Recorder](https://img.youtube.com/vi/VIDEO_ID/0.jpg)]](https://github.com/yunee19/yunee24/assets/133479803/e2f445c0-cfbc-4630-b49d-b90d405bcf0a)

이 프로그램은 다음과 같은 기능을 제공합니다:

1. **카메라 또는 RTSP 스트림에서 비디오 실시간으로 표시**:
   - OpenCV를 사용하여 카메라 또는 RTSP 스트림을 열고 비디오를 미리보기 창에 실시간으로 표시합니다.

2. **비디오 녹화**:
   - 녹화 모드로 전환하면 프로그램은 카메라 또는 RTSP 스트림에서 비디오를 녹화하기 시작합니다.
   - 비디오를 AVI 파일로 기록하기 위해 `cv2.VideoWriter`를 사용합니다.
   - 녹화를 종료하면 비디오는 'VideoRecoder.avi'라는 이름의 AVI 파일로 저장됩니다.

3. **미리보기 모드와 녹화 모드 간 전환**:
   - 미리보기 모드와 녹화 모드 간 전환은 스페이스바를 눌러 수행할 수 있습니다.
   - 녹화 모드에서는 현재 녹화되고 있다는 것을 나타내기 위해 빨간색 원이 표시됩니다.

4. **FPS 조정**:
   - 녹화되는 비디오의 FPS를 설정할 수 있습니다.
   - 기본적으로 FPS는 20.0으로 설정되어 있지만, 프로그램을 실행하기 전에 `set_fps()`를 호출하여 필요한 FPS 값을 설정할 수 있습니다.

5. **프로그램 종료**:
   - 어떤 모드에서든 ESC 키를 눌러 프로그램을 종료할 수 있습니다.

이러한 기능들로 인해 이 프로그램은 카메라 또는 RTSP 스트림에서 비디오를 표시하고 녹화하는 간단하고 유연한 도구가 됩니다.



This code source is reference the skeleton code provided by ChatGPT 


Have a good day ~~
