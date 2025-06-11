# Thought-to-Text-Stream-of-Consciousness

This application will accept a stream of neural data and use AI to parse the data into human-readable text. This is the receiving architecture of the application. 

## Architecture
The data and metadata (label to right, left, up, down) are sent through a websocket intermittently.

There is a websocket that will accept this data, use AI to convert this to text, and respond with text. 


## Process
1. Accept stream of raw EEG data & metadata labels
2. Preprocess the data (notch filters, butterworth bandpass, zero-mean, unit variance, sliding window overlap)
3. Feature extraction (Power Bands [alpha, beta, delta, gamma frequencies])
4. Define a model Architecture
5. Train a model
6. Make a prediction of text given the raw input
7. Return this textual prediction
8. visualize in the frontend (hold a button or enable/disable button to accept & decode incoming thoughts; similar to push-to-talk [push-for-thought])
