# Custom Mediapipe Graphs
Custom graphs for Mediapipe framework.

## Archived (No longer to be continued)
Please check [mp_proctor](https://github.com/sawthiha/mp_proctor.git) as it organizes all the calculators, graphs and the demo application.

## Features
- Extended Face Mesh Graph
    - orientation (With RenderDataCalculator)
    - Eye Blink (With RenderDataCalculator)
    - Minimal Solution with no annotated output

- Extended Selfie Segmentation
    - Standalone (With Apha Channel Mask)
    - Sender (With Red Channel Mask)
    - Receiver (Convert Red Channel Mask to Alpha Channel Mask)

## Requirement
- Mediapipe v0.8.10.2 (Simply checkout on [this commit](https://github.com/google/mediapipe/commit/63e679d9))

## Installation
You simply put this source directory as submodule into `mediapipe/graphs/custom` or anywhere else inside `mediapipe` where you can reference from bazel. Or, simply run the following commands from the `mediapipe` root directory.

```bash
git submodule add https://github.com/sawthiha/mediapipe_graphs.git mediapipe/graphs/custom
```
