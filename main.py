import os
import cv2

counter = 0

output_folder = 'img'
video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv']

os.makedirs(output_folder, exist_ok=True)

for dir_path, dir_list, files in os.walk('video'):  # в директории video лежат распакованные видео из тест.zip
    for file in files:
        if os.path.splitext(file)[1].lower() in video_extensions:
            cap = cv2.VideoCapture(f'video/{file}')
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            percent = 0.015
            num_frames_to_extract = int(total_frames * percent)

            interval = total_frames / num_frames_to_extract

            selected_frame_indices = [int(i * interval) for i in range(num_frames_to_extract)]
            for idx, frame_num in enumerate(selected_frame_indices):
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
                ret, frame = cap.read()
                if ret:
                    cv2.imwrite(f'img/img{counter}.jpg', frame)
                    counter += 1

            cap.release()
