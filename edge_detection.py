import cv2
import numpy as np
import os
import argparse
from multiprocessing import Pool

def process_image(image_path, output_dir, low_threshold, high_threshold):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print(f"Error loading image: {image_path}")
        return None
    
    edges = cv2.Canny(image, low_threshold, high_threshold)
    
    output_path = os.path.join(output_dir, f"edges_{os.path.basename(image_path)}")
    cv2.imwrite(output_path, edges)
    print(f"Processed and saved: {output_path}")
    return output_path

def process_images_in_parallel(image_paths, output_dir, low_threshold, high_threshold):
    with Pool() as pool:
        pool.starmap(process_image, [(image_path, output_dir, low_threshold, high_threshold) for image_path in image_paths])

def main():
    parser = argparse.ArgumentParser(description="Batch process images with Canny edge detection.")
    parser.add_argument("input_dir", help="Directory containing input images")
    parser.add_argument("output_dir", help="Directory to save processed images")
    parser.add_argument("--low_threshold", type=int, default=100, help="Low threshold for Canny edge detection")
    parser.add_argument("--high_threshold", type=int, default=200, help="High threshold for Canny edge detection")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    image_paths = [os.path.join(args.input_dir, img) for img in os.listdir(args.input_dir) if img.endswith(('.png', '.jpg', '.jpeg'))]
    process_images_in_parallel(image_paths, args.output_dir, args.low_threshold, args.high_threshold)

if __name__ == "__main__":
    main()
