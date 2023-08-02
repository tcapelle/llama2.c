# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Logging into Weights and Biases..."
wandb login

echo "Downloading data..."
python download_tokenized.py