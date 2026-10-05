# Energy Based VAD
Energy Based VAD is an algorithm that distinguishes between speech segments and silence segments.

## Overview
I made it to improve computational efficiency through labeling speech segments.
It receives WAV type audio data and binarizes speech segments and silence segments.

## Results
<img width="856" height="581" alt="image-Photoroom (2)" src="https://github.com/user-attachments/assets/fea5f379-99bf-4bc2-a85e-192d0cabd6a9" />


## How It Works
1. Turn the WAV file into a numpy array.
2. Calculate the frame length and the number of frames.
3. Discard the leftover samples that do not fill a full frame.
4. Arrange the samples into frames.
5. Convert the samples arranged in frames into float.
6. Calculate the L2 norm of each frame and their average.
7. Binarize each frame: 1 if its L2 norm is above the average, 0 otherwise.
8. Fill short voids and remove short speech.
9. Plot the result with Matplotlib.

## Getting Started
### Requirements
- Python 3
- NumPy, SciPy, Matplotlib

```bash
pip install numpy scipy matplotlib
```

### Usage
1. Change "example.wav" in line 4 to your file name.
2.  The file type has to be WAV.
3. The file has to be in the same folder as the script.
4. The file has to be mono.
```bash
python energy-based-VAD.py
```

## Limitations
1. It can't find the best threshold, so it deletes small sounds or most sounds(if very big sound is).
2. It needs the whole file
3. It has to wait for future frames 

## Next Steps
- learning-based VAD
- VAP

## License
This project is licensed under the MIT License.
