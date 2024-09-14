# CAShift-Bench

This repo contains replica-package for the Log-Based Anomaly Detection models used in research paper CAShift: Benchmarking Log-Based Cloud Attack Detection under Normality Shift. Including our self-implemented AutoEncoder (AE), Variational AutoEncoder (VAE) model. Different configuration files can be used for reproducing our evaluation experiment such as RQ1: In Distribution Evaluation, RQ2: Shift Scenario Evaluation and RQ3: Continous Learning with Retrain for Shift Adaptation.

## Requrements

python=3.10

Default requirements.txt works on:

NVIDIA-SMI 535.104.12, Driver Version: 535.104.12, CUDA Version: 12.2, Card: NVIDIA L40

* On Server 10.0.104.142:

NVIDIA-SMI 515.65.01, Driver Version: 515.65.01, CUDA Version: 11.7, Card: NVIDIA RTX A5000

```bash
pip uninstall torvision
pip uninstall nvidia-cuda-nvrtc-cu12
pip uninstall nvidia-cuda-cupti-nvrtc-cu12 
pip uninstall nvidia-cuda-cupti-cu12

conda install cudatoolkit=11.7 -c nvidia # Not sure if necessary
pip install torch==1.13.1
```

## Evaluation

<!-- Check whether output dir exist before running `run_train.py` -->

AE.pth and VAE.pth stable trained model

python test_auto.py

python main.py --config=retrain.yaml

## Data

FinalFeature: TSNE Result and All Embedding Files
RetrainFeature: Shift Train Embedding Files
tsne_result.npyL TSNE Data