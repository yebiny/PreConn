# Face Scene Object ROI

![res3](./1-FSO_rio/info/model-block.png)

## 1. 실험 구성

1-FSO_roi\
├── README.md\
├── exe_this.py\
├── make_matrix.py\
├── structure.psyexp\
├── stim\
   ├── face\
   ├── imginfo.txt\
   ├── object\
   └── scene\

## 2. 실험 진행

### 2-1. Make personal matrix
  
```
make_matrix.py [subject_name]
```

* **[subject_name] / matrix** 디렉토리 안에 다음과 같이 1_matrix.csv 파일이 만들어집니다

[subject_name] \
└  data\
└  matrix\
   └─ 1_matrix.csv\
└ personal_info.txt

### 2-2. Run the executable file

```
python exe_this.py [subject_name]
```

* **[subject_name] / matrix / 1_matrix.csv** 파일을 가져오고 그 정보를 바탕으로 실험을 진행합니다. 

### 2-3. Check Data

실험 데이터는 **[subject_name] / data / 'exp_1_..'** 이라는 이름으로 저장됩니다. 
