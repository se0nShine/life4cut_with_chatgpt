import cv2
import numpy as np

def capture_images():
    # 웹캠을 초기화합니다
    cap = cv2.VideoCapture(0)
    captured_images = []

    while True:
        ret, frame = 
        if not ret:
            print("웹캠에서 영상을 읽을 수 없습니다.")
            break
        
        # 현재 프레임을 화면에 보여줍니다
        ('Webcam', frame)

        # 사용자가 'c' 키를 누르면 사진을 캡처합니다
        if cv2.waitKey(1) & 0xFF == ord(''):
            captured_images.append()
            print(f"{len(captured_images)} 장의 사진을 캡처했습니다.")
        
        # 4장의 사진이 모두 캡처되면 루프를 종료합니다
        if len(captured_images) == 4:
            break

    # 웹캠을 해제합니다
    cap.release()
    cv2.destroyAllWindows()

    return captured_images

def display_images(images):
    # 4개의 이미지를 2x2 배열로 보여줍니다
    combined_image = np.zeros((images[0].shape[0] * 2, images[0].shape[1] * 2, 3), dtype=np.uint8)

    combined_image[:images[0].shape[0], :images[0].shape[1]] = images[0]
    combined_image[:images[1].shape[0], images[0].shape[1]:] = images[1]
    combined_image[images[0].shape[0]:, :images[0].shape[1]] = images[2]
    combined_image[images[0].shape[0]:, images[0].shape[1]:] = images[3]

    cv2.imshow('Captured Images', combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    captured_images = capture_images()
    if len(captured_images) == 4:
        display_images(captured_images)

if __name__ == "__main__":
    main()
