import os
import cv2

def generate_reel(folder_path):
    images = []

    for file in os.listdir(folder_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            images.append(os.path.join(folder_path, file))

    if not images:
        return None

    images.sort()

    frame = cv2.imread(images[0])
    height, width, _ = frame.shape

    rec_id = os.path.basename(folder_path)
    output_dir = os.path.join("static", "output")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"{rec_id}.mp4")

    video = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*'mp4v'),
        1,  
        (width, height)
    )

    for image in images:
        frame = cv2.imread(image)
        video.write(frame)

    video.release()

    return f"output/{rec_id}.mp4"