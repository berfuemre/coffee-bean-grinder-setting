import cv2

def analyze_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the average brightness (roast level) of the beans
    avg_brightness = gray.mean()

    # Map the brightness to a grinder setting (1-10 scale)
    if avg_brightness > 180:
        return 1  # Light roast -> finer grind
    elif avg_brightness > 140:
        return 3
    elif avg_brightness > 90:
        return 5
    elif avg_brightness > 60:
        return 7
    else:
        return 10  # Dark roast -> coarser grind
