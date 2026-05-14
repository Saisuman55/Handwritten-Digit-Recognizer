# Handwritten Digit Recognizer

Simple project demonstrating a handwritten digit classifier (MNIST-style) implemented in Keras/TensorFlow. The repository contains the notebook used to train/evaluate the model and helper utilities for inference and CI.

Files of interest
- `Handwritten_Digit_Recognizer_FINAL.ipynb` — notebook with preprocessing, training, and evaluation steps.
- `predict.py` — small CLI to run inference with a saved Keras model.
- `scripts/publish_model_release.sh` — helper to upload the trained model to a GitHub Release (uses `gh` CLI).

Quick start

1. Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Open the notebook:

```bash
jupyter notebook Handwritten_Digit_Recognizer_FINAL.ipynb
```

Inference

Use the included `predict.py` to predict a single image (expects a grayscale 28x28 style digit image, it will resize/convert automatically):

```bash
python predict.py --model digit_recognizer_model.h5 path/to/digit_image.png
```

Model distribution / Releases

Large binary assets (trained models, large PDFs) have been removed from the Git history to keep the repository small. To publish the trained model as a Release asset, use the helper script (requires the GitHub CLI `gh` and an authenticated session):

```bash
./scripts/publish_model_release.sh v1.0.0 path/to/digit_recognizer_model.h5
```

After uploading, users can download the model asset from the corresponding GitHub Release and place it alongside the repository or provide the `--model` path to `predict.py`.

CI and tests

- A minimal GitHub Actions workflow runs linting and `pytest` on pushes and PRs to `main` (`.github/workflows/ci.yml`).
- A smoke test is available at `tests/test_smoke.py`.

Notes about removed files

- `digit_recognizer_model.h5` and `Handwritten_Digit_Recognizer_FINAL.pdf` were removed from the repository history and are now ignored by `.gitignore` to avoid bloating the repo.
- If you need to re-add a model for local testing, download it from the Releases page or place it in a `models/` directory and update `.gitignore` if desired.

Contributing

Contributions are welcome. Open an issue or a pull request for fixes, improvements, or model updates.

License

This project is released under the MIT License. See `LICENSE` for details.

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
