import pandas as pd
import numpy as np
import random
import sys

def make_matrix_file(matrix_data, matrix_index, save_dir, save_name):
    stim_data = pd.DataFrame(matrix_data, index=matrix_index)
    save_as = './subjects/'+save_dir+'/matrix/'+save_name
    stim_data.to_csv(save_as)
    print('This file is :', save_as)
    print(pd.read_csv(save_as))

def select_random_number():
  while True:
    num_overlap_list = [1,2,2,2,3,3]
    overlap_list = random.sample(range(1,11),random.choice(num_overlap_list))
    if len(overlap_list) == 2:
      if abs(overlap_list[0]-overlap_list[1]) > 1:
        return overlap_list
        break
    elif len(overlap_list) == 3:
      if abs(overlap_list[0]-overlap_list[1]) > 1 and abs(overlap_list[0]-overlap_list[2]) > 1 and abs(overlap_list[1]-overlap_list[2]) > 1:
        return overlap_list
        break
    else:
      return overlap_list
      break

def make_matrix_list():
    matrix_list = []
    print("==FaceBlockID ==")
    f_blockID = []
    f_blockID_list = [i+1 for i in range(12)]
    np.random.shuffle(f_blockID_list)
    for i in range(12):
        for j in range(12):
            f_blockID.append(f_blockID_list[i])
    print(f_blockID)
    matrix_list.append(f_blockID)

    print("==SceneBlockID==")
    s_blockID = []
    s_blockID_list = [i+1 for i in range(12)]
    np.random.shuffle(s_blockID_list)
    for i in range(12):
        for j in range(12):
            s_blockID.append(s_blockID_list[i])
    print(s_blockID)
    matrix_list.append(s_blockID)

    print("== Trial ==")
    trial = []
    for i in range(12):
        trial_list = [i+1 for i in range(12)]
        trial.extend(trial_list)
    print(trial)
    matrix_list.append(trial)

    print("== Category ==")
    category = []
    category_list = []
    for i in range(6): category_list.append(1)
    for i in range(6): category_list.append(2)
    random.shuffle(category_list)
    for i in range(12):
        for j in range(12):
            category.append(category_list[i])
    print(category)
    matrix_list.append(category)

    print("=======Face  ImageID=======")
    f_imageID = []
    for i in range(12):
        f_img_idx = [i+1 for i in range(12)]
        np.random.shuffle(f_img_idx)
        f_imageID.extend(f_img_idx)
    print(f_imageID)    
    matrix_list.append(f_imageID)


    print("=======Scene ImageID=======")
    s_imageID = []
    for i in range(12):
        s_img_idx = [i+1 for i in range(12)]
        np.random.shuffle(s_img_idx)
        s_imageID.extend(s_img_idx)
    print(s_imageID)
    matrix_list.append(s_imageID)

    print("=======Target-ness=======")
    target_list = []
    for i in range(12): target_list.append(select_random_number())
    target_ness = []
    for i in range(12):
        for j in range(len(target_list)):
            if j in target_list[i]: 
                target_ness.append(1)
            else: target_ness.append(0)
    print(target_ness)
    matrix_list.append(target_ness)

    print("=======Onset time=======")
    onset_time = []
    time = 0
    for i in range(144):
        if i%12 == 0 and i!=0: time = time+18    
        else: time = time+1.5
        onset_time.append(time)
    print(onset_time)
    matrix_list.append(onset_time)  
    
    matrix_list = np.array(matrix_list, float)
    return matrix_list				

def main():
	matrix_list = make_matrix_list()
	matrix_index = ['f_blockID','s_blockID','trial','category','f_imageID','s_imageID','target_ness', 'onset_time']
	save_dir = sys.argv[1]
	
	if len(sys.argv) == 3:
		save_name = sys.argv[2]
	else:
		save_name = 'matrix.csv'

	make_matrix_file(matrix_list, matrix_index, save_dir, save_name)
if __name__ == '__main__':	
	main()
