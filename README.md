# Image Edge Detection Project

## Description
This project performs edge detection on a batch of images using the Canny edge detection algorithm. The implementation is in Python using OpenCV and supports parallel processing to handle large datasets efficiently.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/image-edge-detection.git
    cd image-edge-detection
    ```
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Prepare your images in a directory (e.g., `input_images`).
2. Run the edge detection script:
    ```sh
    python edge_detection.py input_images output_images --low_threshold 100 --high_threshold 200
    ```

## Example
- Input directory: `input_images/`
- Output directory: `output_images/`

## Proof of Execution
Screenshots or logs showing the execution of the script and the resulting images are included in the `execution_proof` directory.

## Lessons Learned
- Understanding and implementing the Canny edge detection algorithm.
- Efficiently processing large datasets using parallel processing.
- Importance of clear documentation and a well-structured codebase.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
