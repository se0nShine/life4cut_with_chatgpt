import cv2
import numpy as np

def capture_images():
    # 웹캠을 초기화합니다
    cap = cv2.VideoCapture(0)
    captured_images = []

    while True:
        ret, frame = cap.read()
        if not ret:
            print("웹캠에서 영상을 읽을 수 없습니다.")
            break
        
        # 현재 프레임을 화면에 보여줍니다
        cv2.imshow('Webcam', frame)

        # 사용자가 'c' 키를 누르면 사진을 캡처합니다
        if cv2.waitKey(1) & 0xFF == ord('c'):
            captured_images.append(frame)
            print(f"{len(captured_images)} 장의 사진을 캡처했습니다.")
        
        # 4장의 사진이 모두 캡처되면 루프를 종료합니다
        if len(captured_images) == 4:
            break

    # 웹캠을 해제합니다
    cap.release()
    cv2.destroyAllWindows()

    return captured_images

def combine_images_vertically(images, padding=10, gap=10):
    # 이미지가 4장인지 확인합니다
    if len(images) != 4:
        print("이미지가 4장이 아닙니다.")
        return None

    # 각 이미지의 크기를 구합니다
    ,  , _ = images[0].shape

    # 패딩이 적용된 이미지 크기
    padded_height = height + 2 * padding
    padded_width = width + 2 * padding

    # 세로로 결합할 때 전체 높이를 계산합니다 (간격 포함)
    combined_height = padded_height * 4 + gap * 3

    # 빈 이미지(검은색 배경)를 만듭니다
    combined_image = ((combined_height, padded_width, 3), dtype=np.uint8)

    # 이미지를 배치할 때 패딩과 간격을 적용합니다
    for i in range(4):
        y_offset = i * (padded_height + gap)
        combined_image[y_offset + padding:y_offset + padding + height, padding:padding + width] = images[i]

    return combined_image

def main():
    captured_images = capture_images()
    if captured_images and len(captured_images) == 4:
        combined_image = combine_images_vertically(captured_images)
        if combined_image is not None:
            cv2.imshow('Combined Image', combined_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
