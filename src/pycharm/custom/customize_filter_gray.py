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

    # 이미지를 흑백으로 변환합니다
    gray_image = cv2.cvtColor(combined_image, cv2.COLOR_BGR2GRAY)

    return gray_image

def main():
    # 저장된 결합된 이미지 파일 경로
    file_path = 'combined_image_vertical.jpg'

    # 이미지를 불러와서 수정 및 흑백으로 변환
    gray_image = load_and_modify_image(file_path)

    if gray_image is not None:
        # 흑백 이미지를 저장합니다 (예를 들어, 'gray_image.jpg'로 저장)
        cv2.imwrite('gray_image.jpg', gray_image)
        print("흑백 이미지를 'gray_image.jpg'로 저장했습니다.")
        
        # 흑백 이미지를 표시합니다
        cv2.imshow('Grayscale Image', gray_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
