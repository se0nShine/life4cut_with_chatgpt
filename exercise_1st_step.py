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
            ################### Question 1. 아래에 들어갈 코드(1줄)를 작성해보세요. ##########
            ## Hint : 리스트에 새 원소를 더할때는 (리스트).append(원소)를 이용합니다.        ##
            None 
            ###############################################################################
            print(f"{len(  captured_images )} 장의 사진을 캡처했습니다.")
        
        # 사진이 모두 캡처되면 루프를 종료합니다
        if len(captured_images) == None: ### Question 2. None 대신에 올바른 숫자를 입력해 보세요. ###
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
        ##################### Question 3. 아래에 들어갈 코드(1줄)를 작성해보세요. #####################
        ## None을 지우고 그 자리에 작성하면 됩니다. 
        ## Hint : 이미지를 보여줄 수 있는 기능을 담은 함수를 호출하고, 어떤 값이 들어가야하는지 생각해보세요.
        ## Example. 
        ##          def add_one(x):
        ##              return x + 1
        ##          3+1을 연산하고 싶다면 add_one(3)을 호출하면 된다.
        None 
        ##############################################################################################

if __name__ == "__main__":
    main()
