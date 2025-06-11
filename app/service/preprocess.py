"""
## Module Purpose:
1. Accept stream of raw EEG data & metadata labels
2. Preprocess the data (notch filters, butterworth bandpass, zero-mean, unit variance, sliding window overlap)
3. Feature extraction (Power Bands [alpha, beta, delta, gamma frequencies])
4. Define a model Architecture
5. Train a model
6. Make a prediction of text given the raw input
7. Return this textual prediction
8. visualize in the frontend (hold a button or enable/disable button to accept & decode incoming thoughts; similar to push-to-talk [push-for-thought])
"""