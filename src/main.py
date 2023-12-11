from ultralytics import YOLO

# n s m l x

def test():
    model = YOLO('yolov8x.pt')
    results = model.train(data='./tt100k_2021/tt100k_2021.yaml', epochs=8, device=[0,1,2,3], batch=32)

def serious():
    model = YOLO('yolov8x.pt')
    results = model.train(data='./tt100k_2021/tt100k_2021.yaml', epochs=400, device=[0,1,2,3], batch=32)

def resume():
    model = YOLO('./runs/detect/train2/weights/last.pt')
    results = model.train(resume=True)

if __name__ == '__main__':
    serious()