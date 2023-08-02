# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Downgrade Protobuf"
pip install "protobuf==3.20"

echo "Logging into Weights and Biases..."
wandb login

echo "Downloading data..."
python download_tokenized.py