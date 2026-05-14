# Handwritten Digit Recognizer

This repository contains a Jupyter notebook demonstrating a handwritten digit recognizer (MNIST-like). It includes the trained model file `digit_recognizer_model.h5` and the notebook `Handwritten_Digit_Recognizer_FINAL.ipynb`.

Files
- `Handwritten_Digit_Recognizer_FINAL.ipynb` — analysis, preprocessing, model training and evaluation notebook.
- `digit_recognizer_model.h5` — trained Keras model weights.

Quick start

1. Create a Python environment (recommended):

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Launch the notebook:

```bash
jupyter notebook Handwritten_Digit_Recognizer_FINAL.ipynb
```

Notes
- The trained model file `digit_recognizer_model.h5` is included. If you prefer not to commit large model files, move it to `models/` and add that path to `.gitignore`.
