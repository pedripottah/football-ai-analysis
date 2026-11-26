import cv2

# Splits video into list of Numpy image frames
def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames

# Stiches those frames back into a .avi video (24 FPS)
def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(
        output_video_path,
        fourcc,
        24,
        (output_video_frames[0].shape[1], output_video_frames[0].shape[0])
    )
    for frame in output_video_frames:
        out.write(frame)
    out.release()