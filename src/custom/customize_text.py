import cv2
import numpy as np

def load_and_modify_image(file_path):
    # 이미지 파일을 불러옵니다
    combined_image = cv2.imread(file_path)

    if combined_image is None:
        print(f"{file_path} 파일을 읽을 수 없습니다.")
        return

    # 검정색 배경을 흰색으로 변경합니다 (예시로 추가)
    combined_image[np.where((combined_image == [0,0,0]).all(axis=2))] = [255, 255, 255]

    # 이미지에 텍스트를 추가합니다
    text = "Hello, OpenCV!"
    org = (50, 50)  # 텍스트의 좌측 상단 시작 위치
    fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 폰트 선택
    fontScale = 1  # 폰트 크기
    color = (255, 0, 0)  # 텍스트 색상 (BGR 형식)
    thickness = 2  # 선 두께

    combined_image = cv2.putText(combined_image, text, org, fontFace, fontScale, color, thickness, cv2.LINE_AA)

    return combined_image

def main():
    # 저장된 결합된 이미지 파일 경로
    file_path = 'combined_image_vertical.jpg'

    # 이미지를 불러와서 수정 및 텍스트 추가
    modified_image = load_and_modify_image(file_path)

    if modified_image is not None:
        # 수정된 이미지를 저장합니다 (예를 들어, 'modified_image_with_text.jpg'로 저장)
        cv2.imwrite('modified_image_with_text.jpg', modified_image)
        print("텍스트가 추가된 이미지를 'modified_image_with_text.jpg'로 저장했습니다.")
        
        # 수정된 이미지를 표시합니다
        cv2.imshow('Modified Image with Text', modified_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
