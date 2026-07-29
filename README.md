# Allo AI 🤖

Allo AI is a Python chatbot project with two models:

## Allo 1.0 Fast
- Lightweight chatbot
- Quick responses
- Good for testing and learning

## Allo 1.0 Pro
- More advanced chatbot logic
- Larger response system
- Ready for future AI model upgrades

## Features
- Python CLI chatbot
- TensorFlow/Keras neural network training
- Training data support
- Saved AI model (`allo_model.h5`)
- Easy to customize

## Setup

Create the TensorFlow environment:

```bash
python3.12 -m venv tf_env
source tf_env/bin/activate
```

Windows PowerShell:

```powershell
.\tf_env\Scripts\Activate.ps1
```

Install packages:

```bash
pip install -r requirements.txt
```

## Train Allo Neural Network

```bash
python train.py
```

This creates:

```
allo_model.h5
 tokenzier.pkl
labels.pkl
```

## Run

```bash
python allo_fast.py
```

or

```bash
python allo_pro.py
```

## Files

```
allo_fast.py      # Allo 1.0 Fast
allo_pro.py       # Allo 1.0 Pro
train.py          # TensorFlow/Keras trainer
train_data.json   # Training examples
requirements.txt  # Python packages
allo_model.h5     # Trained model output
```

## Roadmap
- Better memory
- Web chatbot interface
- Allo API
- Larger AI models
