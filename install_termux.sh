#!/bin/bash

echo "[*] ETCHERO-MULTITOOL-V3 Installer for Termux"
echo "[*] Updating packages..."
pkg update -y && pkg upgrade -y

echo "[*] Installing Python and dependencies..."
pkg install python git -y

echo "[*] Installing Python libraries..."
pip install -r requirements.txt

echo "[*] Setup complete! You can now run the tool with:"
echo "python ETCHERO.py"
