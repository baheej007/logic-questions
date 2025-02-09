import multiprocessing
import ffmpeg

def convert_video(video_file):
    output_file = f"compressed_{video_file}"
    ffmpeg.input(video_file).output(output_file, vcodec="libx264", crf=23).run()
    print(f"Converted {video_file} -> {output_file}")

videos = ["video1.mp4", "video2.mp4", "video3.mp4"]

if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        pool.map(convert_video, videos)