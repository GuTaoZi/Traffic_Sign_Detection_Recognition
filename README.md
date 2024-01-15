

## Traffic-Sign Detection and Recognition

This project refines YOLOv8 for traffic sign detection and recognition(TSDR) with attention modules.

Base model: [YOLOv8 Extra Large (YOLOv8x)](https://github.com/ultralytics/ultralytics)

Attention modules: SE and ECA

Dataset: [Tsinghua-Tencent 100K](https://cg.cs.tsinghua.edu.cn/traffic-sign/) and SUSTech custom test set.

Platform: 4 * GeForce RTX 2080 Ti, Intel(R) Xeon(R) Gold 6240 CPU @ 2.60GHz, SUSTech GPULab02 of CSE.

Project for SUSTech Course CS329 Machine Learning(H).

<img src="https://s2.loli.net/2024/01/15/eZsEb1Uy97zuj5N.png" alt="image.png" style="zoom: 33%;" />

For experiments and results, please see our [research report](https://github.com/GuTaoZi/Traffic_Sign_Detection_Recognition/blob/main/doc/Traffic-Sign%20Detection%20and%20Recognition(final%20report).pdf).

```C
Traffic_Sign_Detection_Recognition
├─custom_testset
│  ├─images
│  └─videos
├─doc
│  └─img
├─models
│  ├─YOLOv8n
│  │  └─weights
│  ├─YOLOv8x
│  │  └─weights
│  ├─YOLOv8x_ECA
│  │  └─weights
│  └─YOLOv8x_SE
│      └─weights
├─src
│  ├─preprocesser
│  └─ultralytics
└─tt100k_2021
    ├── images
    │   ├── other
    │   ├── test
    │   ├── train
    │   └── val
    ├── labels
    │   ├── other
    │   ├── test
    │   ├── train
    │   └── val
    └── marks
```

