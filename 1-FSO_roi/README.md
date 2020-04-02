# Face Scene Object ROI


1-FSO_roi\
├── README.md\
├── exe_this.py\
├── make_matrix.py\
├── structure.psyexp\
├── stim\
   ├── face\
   ├── imginfo.txt\
   ├── object\
   └── scene

## 1. 실험 구성

![res3](info/model-block.png)


![res3](info/model-trial.png)


* 12개의 Block 으로 이루어져 있습니다.
* Block의 종류는 총 3가지, Face, Scene, Object로 이루어져 있습니다.
* 한 Block이 시행되면 Block 종류에 따른 12개의 이미지가 각 trial마다 출력됩니다. 
* 한 Block은 1.5 * 12 = 총 18초 입니다.  
* 한 Block이 끝나면 12초 동안 Rest 단계가 있습니다.
* 이미지는 Face, Scene, Object 각각 48장이 존재합니다.
* target은 한 블럭 안에 최소 1번에서 최대 3번까지 랜덤으로 존재합니다.
* target 일때 이미지는 직전 이미지와 동일한 이미지가 출력됩니다. 



## 2. 실험 진행

### 2-1. Make personal matrix

#### Matrix format

|  <center>Unnamed</center> |  <center>0</center> |  <center>1</center> |  <center>2</center> |  <center>3</center> |  <center>4</center> |
|:--------|:--------:|--------:|--------:|--------:|--------:|
|**blockID** | <center> 1 </center> |<center> 1 </center> |<center> 1 </center> |<center> 1 </center> |<center> ... </center> |
|**trial** | <center> 1 </center> |<center> 2 </center> |<center> 3 </center> |<center> 4 </center> |<center> ... </center> |
|**category** | <center> 3 </center> |<center> 1 </center> |<center> 1 </center> |<center> 1 </center> |<center> ... </center> |
|**imageID** | <center> 28 </center> |<center> 1 </center> |<center> 1 </center> |<center> 1 </center> |<center> ... </center> |
|**target_ness** | <center> 0 </center> |<center> 0 </center> |<center> 1 </center> |<center> 0 </center> |<center> ... </center> |
|**onset_time** | <center> 0 </center> |<center> 1.5 </center> |<center> 3 </center> |<center> 4.5 </center> |<center> ... </center> |

* blockID:
* trial:
* category:
* imageID:
* target_ness:
* onset_time:


#### Make matrix.csv file


```
python make_matrix.py [subject_name]
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

* 실험 데이터는 'exp_1_..' 이라는 이름으로  ** [subject_name] / data / **에 아래와 같이 저장됩니다.
