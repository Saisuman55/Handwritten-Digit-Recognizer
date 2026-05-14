import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image

try:
    from tensorflow.keras.models import load_model
except Exception:
    print("TensorFlow not installed. Install requirements.txt before running.")
    raise


def preprocess_image(img_path: Path):
    img = Image.open(img_path).convert("L")
    img = img.resize((28, 28))
    arr = np.array(img).astype("float32") / 255.0
    arr = arr.reshape(1, 28, 28, 1)
    return arr


def predict(model_path: Path, image_path: Path):
    model = load_model(str(model_path))
    x = preprocess_image(image_path)
    preds = model.predict(x)
    label = int(np.argmax(preds, axis=1)[0])
    return label, preds


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", "-m", type=Path, default=Path("digit_recognizer_model.h5"))
    p.add_argument("image", type=Path, help="Path to input image (PNG/JPG)")
    args = p.parse_args()

    if not args.model.exists():
        print(f"Model file not found: {args.model}")
        sys.exit(2)
    if not args.image.exists():
        print(f"Image file not found: {args.image}")
        sys.exit(2)

    label, preds = predict(args.model, args.image)
    print(f"Predicted label: {label}")


if __name__ == "__main__":
    main()
