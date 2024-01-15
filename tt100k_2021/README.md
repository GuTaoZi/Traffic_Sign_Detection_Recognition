## Dataset Setup

The dataset used for training our model is [**Tsinghua-Tencent 100K**](https://cg.cs.tsinghua.edu.cn/traffic-sign/), you may check the tutorial [here](https://cg.cs.tsinghua.edu.cn/traffic-sign/tutorial.html).

The dataset is not uploaded since the dataset is large, please download and unzip manually:

```sh
wget http://cg.cs.tsinghua.edu.cn/traffic-sign/data_model_code/data.zip
unzip data.zip
```

Then we execute the python script `dataSplitter.py` under the `src/preprocessor` folder to split the dataset.

The dataset folder should be in this structure:

```
tt100k_2021/
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

Then execute `dataNormalizer.py` under the `src/preprocessor` folder to normalize the dataset for YOLO usages.