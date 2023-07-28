import os
import argparse
from multiprocessing import Pool

def findAllFile(base):
    file_path = []
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            file_path.append(fullname)
    return file_path

def convert(video_path):
    video_name = video_path.split('/')[-1]
    image_path = video_path.replace(video_name, video_name.split('.')[0])
    image_path = image_path.replace('/videos/', '/images/')
    os.makedirs(image_path, exist_ok=True)
    os.system(f'ffmpeg -i {video_path} -f image2 -r 30 -b:v 5626k {image_path}/%06d.png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_folder', type=str, default='data/UBody/videos')
    args = parser.parse_args()
    video_paths = findAllFile(args.video_folder)
    pool = Pool(processes=8)
    pool.map(convert, video_paths)
    pool.close()
    pool.join()