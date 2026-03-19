import os
import cv2

def generate_reel(folder_path):
    images = []

    # Collect image files
    for file in os.listdir(folder_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            images.append(os.path.join(folder_path, file))

    if not images:
        return None

    # Sort images (optional)
    images.sort()

    # Read first image to get size
    frame = cv2.imread(images[0])
    height, width, _ = frame.shape

    # Output path
    rec_id = os.path.basename(folder_path)
    output_dir = os.path.join("static", "output")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"{rec_id}.mp4")

    # Video writer
    video = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*'mp4v'),
        1,  # 1 FPS (change if needed)
        (width, height)
    )

    for image in images:
        frame = cv2.imread(image)
        video.write(frame)

    video.release()

    return f"output/{rec_id}.mp4"