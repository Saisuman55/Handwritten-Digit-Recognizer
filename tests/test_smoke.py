from pathlib import Path


def test_files_exist():
    repo_root = Path(__file__).resolve().parents[1]
    assert (repo_root / "Handwritten_Digit_Recognizer_FINAL.ipynb").exists()
    assert (repo_root / "README.md").exists()
