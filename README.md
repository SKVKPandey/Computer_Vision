
# Computer_Vision

This repository contains python programs related to computer vision.  
As of now, the files related to Hand Landmarks, Face Landmarks, Face Detection and Body Landmarks has been added.

## Technologies Used
- Python
- OpenCV
- MediaPipe

## About the Project

- The folder contains the following files: `Hand.py`, `FaceDet.py`, `FaceMesh.py` and `PoseEst.py`.
[![2.png](https://i.postimg.cc/DfcXPwry/2.png)](https://postimg.cc/BtXbqs7d)
- `Hand.py` is the file that detects the Hand Landmarks and show connections between the landmarks.
[![3.png](https://i.postimg.cc/rsZ7LLr0/3.png)](https://postimg.cc/2Lv04MTr)
- `FaceDet.py` is the file that detects Face and also tells about how much portion of the face is detectable.
[![1.png](https://i.postimg.cc/HLCYNQHG/1.png)](https://postimg.cc/dh4ckZLn)
- `FaceMesh.py` is the file that detects Face Landmarks and Face Mesh.
[![4.png](https://i.postimg.cc/PxvkrJdb/4.png)](https://postimg.cc/MMwL9WMX)
- `PoseEst.py` is the file that detects Body Landmarks and show connections of Landmarks according to the pose. 

## Video Sample

For the Demo check out this video: https://vimeo.com/697684123

## Run Locally

Clone the project

```bash
  git clone https://github.com/SKVKPandey/Computer_Vision.git
```

Go to the project directory

```bash
  cd Computer_Vision
```

Install virtual environment

```bash
  virtualenv venv
```

Activate the virtual environment (for Git Bash)

```bash
  source venv/Scripts/activate
```

Install dependencies

```bash
  pip install opencv-python
```
```bash
  pip install mediapipe
```

Run the files
```bash
  python Hand.py
```


## Acknowledgements

 - [OpenCV](https://opencv.org/)
 - [MediaPipe](https://google.github.io/mediapipe/)



## Author

[@SKVKPandey](https://github.com/SKVKPandey)


## License

[MIT](https://github.com/SKVKPandey/Computer_Vision/blob/main/LICENSE)



## Appendix

The repository will be updated soon with python modules containing the basic codes for generating the outputs, so that it could be used in futher projects and there should be no need for repeating the same code.

