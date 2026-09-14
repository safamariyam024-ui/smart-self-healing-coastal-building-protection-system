import cv2
import os


def detect_crack(image_path):
    # Check whether the image exists
    if not os.path.exists(image_path):
        print("ERROR: Image file not found.")
        return None

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("ERROR: Could not read the image.")
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges
    edges = cv2.Canny(blurred, 50, 150)

    # Threshold for dark crack-like regions
    _, threshold = cv2.threshold(
        blurred, 100, 255, cv2.THRESH_BINARY_INV
    )

    # Remove small noise
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (3, 3)
    )

    cleaned = cv2.morphologyEx(
        threshold,
        cv2.MORPH_OPEN,
        kernel
    )

    # Find possible crack contours
    contours, _ = cv2.findContours(
        cleaned,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Copy image for annotation
    result = image.copy()

    crack_area = 0
    crack_count = 0

    # Draw detected regions
    for contour in contours:

        area = cv2.contourArea(contour)

        # Ignore very small regions
        if area > 20:
            crack_count += 1
            crack_area += area

            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                result,
                (x, y),
                (x + w, y + h),
                (0, 0, 255),
                2
            )

    # Calculate approximate crack percentage
    total_pixels = image.shape[0] * image.shape[1]

    crack_percentage = (
        crack_area / total_pixels
    ) * 100

    # Add information to image
    cv2.putText(
        result,
        f"Detected regions: {crack_count}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    cv2.putText(
        result,
        f"Crack area: {crack_percentage:.2f}%",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    # Create output folder
    os.makedirs("outputs", exist_ok=True)

    output_path = "outputs/crack_detection_result.jpg"

    # Save result
    cv2.imwrite(output_path, result)

    print("--------------------------------")
    print("COMPUTER VISION ANALYSIS")
    print("--------------------------------")
    print(f"Detected regions : {crack_count}")
    print(f"Crack area       : {crack_percentage:.2f}%")
    print(f"Result saved to  : {output_path}")

    return {
        "crack_count": crack_count,
        "crack_percentage": crack_percentage,
        "output_path": output_path
    }


# Test the system
if __name__ == "__main__":

    image_path = input(
        "Enter the path of the crack image: "
    )

    detect_crack(image_path)