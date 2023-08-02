from pathlib import Path
import wandb

from tinystories import download

print("downloading dataset")
download()

api = wandb.Api()
artifact = api.artifact('capecape/llamac/tinystories:v1', type='dataset')
artifact_dir = artifact.download()

DATASET_DIR = Path("data/TinyStories_all_data")
# DATASET_DIR = Path("data/test")
DATASET_DIR.mkdir(parents=True, exist_ok=True)


bin_files = Path(artifact_dir).rglob("*.bin")

# copy bin file to DATASET_DIR
print(f"copying bin files to {DATASET_DIR}")
for bin_file in bin_files:
    bin_file.rename(DATASET_DIR / bin_file.name)
