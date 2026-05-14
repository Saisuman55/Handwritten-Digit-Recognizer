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

Inference script

You can use `predict.py` to load a saved model and predict a single image:

```bash
python predict.py --model digit_recognizer_model.h5 path/to/digit_image.png
```

CI

A minimal GitHub Actions workflow runs linting and the smoke test on pushes and PRs to `main`.

Model release

Large model files are removed from the repository history. To attach the trained model to a GitHub Release, use the included helper script (requires GitHub CLI `gh` authenticated):

```bash
./scripts/publish_model_release.sh v1.0.0 path/to/digit_recognizer_model.h5
```

This creates a draft release and uploads the model as an asset; promote the release in the GitHub UI when ready.
