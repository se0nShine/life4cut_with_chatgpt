import cv2
import numpy as np

def load_and_modify_image(file_path):
    # 이미지 파일을 불러옵니다
    combined_image = cv2.imread(file_path)

    if combined_image is None:
        print(f"{file_path} 파일을 읽을 수 없습니다.")
        return

    # 검정색 배경을 흰색으로 변경합니다
    combined_image[np.where((combined_image == [0,0,0]).all(axis=2))] = [255, 255, 255]

    return combined_image

def main():
    # 저장된 결합된 이미지 파일 경로
    file_path = '/content/combined_image_vertical.jpg'

    # 이미지를 불러와서 수정합니다
    modified_image = load_and_modify_image(file_path)

    if modified_image is not None:
        # 수정된 이미지를 저장합니다 (예를 들어, 'modified_image.jpg'로 저장)
        cv2.imwrite('modified_background.jpg', modified_image)
        print("수정된 이미지를 'modified_image.jpg'로 저장했습니다.")
        
        # 수정된 이미지를 표시합니다
        cv2.imshow('Modified Image', modified_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
