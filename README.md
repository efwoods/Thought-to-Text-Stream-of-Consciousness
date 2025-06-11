# Thought-to-Text-Stream-of-Consciousness

This application will accept a stream of neural data and use AI to parse the data into human-readable text. This is the receiving architecture of the application. 

## Architecture
The data and metadata (label to right, left, up, down) are sent through a websocket intermittently.

There is a websocket that will accept this data, use AI to convert this to text, and respond with text. 
