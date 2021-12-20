Camera4Kivy Tensoflow Lite Example
==================================

*Tensorflow Lite Image Analysis using Camera4Kivy*

# Overview

Uses Tensoflow Lite to classify objects in the image stream, classified objects are boxed and labeled in the Preview. 

Available on some of the [usual platforms](https://github.com/Android-for-Python/Camera4Kivy/#tested-platforms).

This example is based on a [Tensorflow Lite Object Detection Example](https://github.com/tensorflow/examples/tree/master/lite/examples/object_detection/raspberry_pi). This example was trained on the [COCO dataset](https://cocodataset.org/#home).

As of 2021/12/13 the Python `tflite_runtime.whl` is not available for any of Python 3.10, MacOS on M1, MacOS Monterey, iOS, x86_32, or Android. **If you use any of these, stop now**. If you have a problem with this talk to Google.

# Image Analysis Architecture

Tensorflow Image analysis has four distinct components:

- The tensorflow lite model, formated to include tensor labels.

- The Python tflite-runtime package. This performs inference based on the model and the input image. This package is available from Google on most desktops.

- The model interface, specific to the tflite model [object_detection/object_detector.py](https://github.com/Android-for-Python/c4k_tflite_example/object_detection/object_detector.py). This encodes the model input, executes the runtime, and decodes the output.

- The Camera4Kivy interface [classifyobject.py](https://github.com/Android-for-Python/c4k_tflite_example/classifyobject.py). This passes the image to the model interface, and annotates the output to the Preview.

# Install

This example depends on [Camera4Kivy](https://github.com/Android-for-Python/Camera4Kivy#camera4kivy). Depending on the platform you may need to install a [camera provider](https://github.com/Android-for-Python/Camera4Kivy#dependencies). 

## Windows, MacOS x86_64, Linux
`pip3 install numpy opencv-python camera4kivy`

The currently available version of tflite-runtime maybe different to the one used on the next line.

`pip3 install --index-url https://google-coral.github.io/py-repo/  tflite-runtime==2.5.0.post1`

If you use a [Coral Accelerator](https://coral.ai/products/accelerator) set `enable_edgetpu = True` in `classifyobject.py`.



