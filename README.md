# Custom Mediapipe Graphs
Custom graphs for Mediapipe framework.

## Features
- Extended Face Mesh Graph
    - Alignment (With RenderDataCalculator)
    - Eye Blink (With RenderDataCalculator)

- Extended Selfie Segmentation
    - Standalone (With Apha Channel Mask)
    - Sender (With Red Channel Mask)
    - Receiver (Convert Red Channel Mask to Alpha Channel Mask)

## Installation
You simply put this source directory as submodule into `mediapipe/graphs/custom` or anywhere else inside `mediapipe` where you can reference from bazel. Or, simply run the following commands from the `mediapipe` root directory.

```bash
git submodule add https://github.com/sawthiha/mediapipe_graphs.git mediapipe/graphs/custom
```
