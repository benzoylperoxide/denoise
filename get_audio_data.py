import os
import subprocess

cwd = os.getcwd()
data_dir = os.path.join(cwd, "data")
raw_dir = os.path.join(data_dir, "raw")

def download_datasets(path):
    os.makedirs(path, exist_ok=True)
    librispeech_file = os.path.join(path, "dev-clean.tar.gz")
    esc50_file = os.path.join(path, "master")  # This is a directory name after extraction

    # Download LibriSpeech dataset if not already present
    if not os.path.exists(librispeech_file):
        print("Downloading LibriSpeech dataset...")
        subprocess.run(["wget", "-P", path, "http://openslr.elda.org/resources/12/dev-clean.tar.gz"], check=True)
    else:
        print("LibriSpeech dataset already exists, skipping download.")

    # Download ESC-50 dataset if not already present
    if not os.path.exists(esc50_file):  # Adjust filename if needed based on extraction naming convention
        print("Downloading ESC-50 dataset...")
        subprocess.run(["wget", "-P", path, "https://codeload.github.com/karolpiczak/ESC-50/zip/refs/heads/master"], check=True)
    else:
        print("ESC-50 dataset already exists, skipping download.")

def install_librispeech():
    os.makedirs(raw_dir, exist_ok=True)
    librispeech_file = os.path.join(raw_dir, "dev-clean.tar.gz")
    librispeech_dir = os.path.join(data_dir, "LibriSpeech")

    # Check if installation is already complete
    if os.path.exists(os.path.join(librispeech_dir, "dev-clean")):  # Adjust this condition based on expected structure
        print("LibriSpeech already installed, skipping extraction.")
        return

    os.makedirs(librispeech_dir, exist_ok=True)

    # Extract the LibriSpeech dataset to ./data/LibriSpeech
    if os.path.exists(librispeech_file):
        print("Extracting LibriSpeech dataset...")
        subprocess.run(["tar", "-xzvf", librispeech_file, "-C", librispeech_dir, "--strip-components=1"], check=True)
    else:
        print("LibriSpeech archive not found, extraction skipped.")

def install_esc50():
    esc50_file = os.path.join(raw_dir, "master")
    esc50_dir = os.path.join(data_dir, "ESC-50")
    
    # Check if installation is already complete
    if os.path.exists(os.path.join(esc50_dir, "ESC-50-master")):  # Adjust this condition based on expected structure
        print("ESC-50 already installed, skipping extraction.")
        return

    os.makedirs(esc50_dir, exist_ok=True)

    # Extract the ESC-50 dataset to ./data/ESC-50
    if os.path.exists(esc50_file):
        print("Extracting ESC-50 dataset...")
        subprocess.run(["unzip", "-o", esc50_file, "-d", esc50_dir], check=True)
    else:
        print("ESC-50 archive not found, extraction skipped.")
