# yolov5-global-currency

1) 핵심 설정파일

  - data/custom.yaml

  - datasets/global-currency/train.txt

  - datasets/global-currency/val.txt

  - datasets/global-currency/test.txt

2) train / val / test 텍스트파일 생성 로직

  - makelist.py

3) 기계학습 명령

```python
python train.py --img 640 --batch 16 --epochs 3 --data custom.yaml --weights yolov5x.pt
```
