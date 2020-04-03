# Face Scene Object ROI


**실험목표**

## 1. 실험 구성

![res3](info/model-block.png)


![res3](info/model-trial.png)


* 이 실험은 12개의 Block 으로 이루어져 있습니다.
* 한 Block은 시간은 18s 입니다.  
* 한 Block이 끝나면 12s 동안 Rest 단계가 있습니다.
* Block의 종류는 총 3가지, Face, Scene, Object로 이루어져 있습니다.
* 한 Block이 시행되면 Block 종류에 따른 12개의 이미지가 각 trial마다 출력됩니다. 
* 이미지는 0.5s 동안 출력됩니다. 
* 이후에는 1s 동안 빈화면이 출력됩니다.
* 이미지는 Face, Scene, Object 각각 4(block) * 12(trial) 48장씩 존재합니다.
* 이미지의 순서는 랜덤합니다.
* target은 한 블럭 안에 최소 1번에서 최대 3번까지 랜덤으로 존재합니다.
* target일때 이미지는 직전 이미지와 동일한 이미지가 출력됩니다. 


## 2. 실험 준비

### 2-1. Make personal matrix

#### Matrix format

|  <center>Unnamed</center> |  <center>0</center> |  <center>1</center> |  <center>2</center> |  <center>3</center> |  <center>4</center> |<center>5</center> | <center>6</center> | <center>7</center> | <center>8</center> | <center>9</center> | <center>3</center> | 
|:--------|:--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
|**blockID** | <center> 1 </center> |<center> 1 </center> |<center> 1 </center> |<center> 1 </center> |<center> 1 </center> |<center> 1 </center> |<center> 1 </center> |<center> 1 </center> |<center> 1 </center> |<center> 1 </center> |<center> ... </center> |
|**trial** | <center> 1 </center> |<center> 2 </center> |<center> 3 </center> |<center> 4 </center> |<center> 5 </center> |<center> 6 </center> |<center> 7</center> |<center> 8 </center> |<center> 9 </center> |<center> 10 </center> |<center> ... </center> |
|**category** | <center> 3 </center> |<center> 3 </center> |<center> 3 </center> |<center> 3</center> |<center> 3 </center> |<center> 3 </center> |<center> 3</center> |<center> 3 </center> |<center> 3 </center> |<center> 3 </center> |<center> ... </center> |
|**imageID** | <center> 28 </center> |<center> 19 </center> |<center> 8 </center> |<center> 4 </center> |<center> 1 </center> |<center> 12 </center> |<center> 21 </center> |<center> 13 </center> |<center> 31 </center> |<center> 43 </center> |<center> ... </center> |
|**target_ness** | <center> 0 </center> |<center> 0 </center> |<center> 1 </center> |<center> 0 </center> |<center> 0 </center> |<center> 0 </center> |<center> 1 </center> |<center> 0 </center> |<center> 0 </center> |<center> 0 </center> |<center> ... </center> |
|**onset_time** | <center> 0 </center> |<center> 1.5 </center> |<center> 3 </center> |<center> 4.5 </center> |<center> 6 </center> |<center> 7.5 </center> |<center> 9 </center> |<center> 10.5 </center> |<center> 12 </center> |<center> 13.5 </center> |<center> ... </center> |

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

* [ subject_name ]/matrix 에 **1_matrix.csv** 파일이 만들어집니다

><img src="info/tree.png" width="230">


## 3. 실험 진행

### 3-1. Run the executable file

```
python exe_this.py [subject_name]
```

* [ subject_name ] 의 matrix 파일을 가져와 그 정보를 바탕으로 실험이 진행합니다. 


### 3-2. Check Data

* 데이터는 **[subject_name] / data /** 에 아래와 같이 저장됩니다.

><img src="info/tree-data.png" width="380">

---
