#!/usr/bin/env bash
# Upload the model file to a GitHub release using the `gh` CLI.
# Usage: ./scripts/publish_model_release.sh v1.0.0 path/to/digit_recognizer_model.h5

set -euo pipefail

TAG=${1:-}
MODEL_PATH=${2:-}

if [[ -z "$TAG" || -z "$MODEL_PATH" ]]; then
  echo "Usage: $0 <tag> <model-file-path>"
  exit 2
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "gh CLI not found. Install from https://github.com/cli/cli and authenticate first."
  exit 1
fi

if [[ ! -f "$MODEL_PATH" ]]; then
  echo "Model file not found: $MODEL_PATH"
  exit 2
fi

# Create a draft release (or update existing)
echo "Creating/updating release $TAG..."
gh release create "$TAG" "$MODEL_PATH" --draft --title "Model $TAG" --notes "Trained digit recognizer model"

echo "Uploaded $MODEL_PATH to release $TAG (draft). Promote draft via GitHub UI when ready."
