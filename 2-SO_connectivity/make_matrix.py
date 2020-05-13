import pandas as pd
import numpy as np
import random
import sys

def make_matrix_file(matrix_data, matrix_index, save_dir, save_name):
    stim_data = pd.DataFrame(matrix_data, index=matrix_index)
    save_as = '../subjects/'+save_dir+'/matrix/'+save_name
    stim_data.to_csv(save_as)
    print('This file is :', save_as)
    print(pd.read_csv(save_as))

def select_random_number(target_count):
  while True:
    overlap_list = random.sample(range(1,11),target_count)
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
    #print("==BlockID==")
    blockID = []
    blockID_list = [i+1 for i in range(12)]
    for i in range(12):
        for j in range(12):
            blockID.append(blockID_list[i])
    #print(blockID)
    matrix_list.append(blockID)

    #print("== Trial ==")
    trial = []
    for i in range(12):
        trial_list = [i+1 for i in range(12)]
        trial.extend(trial_list)
    #print(trial)
    matrix_list.append(trial)

    #print("=======Scene ImageID=======")
    s_imageID = [i+1 for i in range(144)]
    np.random.shuffle(s_imageID)
    matrix_list.append(s_imageID)
    
    #print("=======Object  ImageID=======")
    o_imageID = [i+1 for i in range(144)]
    np.random.shuffle(o_imageID)
    matrix_list.append(o_imageID)
    
    # Condition (Do Not Repeat Same Image!)
    for i in range(48):
        cond_s = s_imageID.count(i+1)
        cond_o = o_imageID.count(i+1)
        if cond_s and cond_o != 1:
            print("Condition did not satisfied.")
            exit()

    #print("=======Target-ness=======")

    target_count = [1 for i in range(12)]
    add_1 = random.sample([i for i in range(12)], 6)
    add_2 = random.sample([i for i in range(12)], 6)
    for i in range(6):
        target_count[add_1[i]] += 1
        target_count[add_2[i]] += 1
    print(target_count, sum(target_count))

    target_list = []
    for i in range(12): 
        target_list.append(select_random_number(target_count[i]))
    
    print(target_list)
    target_ness = []
    for i in range(12):
        for j in range(len(target_list)):
            if j in target_list[i]: 
                target_ness.append(1)
            else: target_ness.append(0)
    print(target_ness)
    matrix_list.append(target_ness)

    #print("=======Onset time=======")
    onset_time = []
    time = 0
    for i in range(144):
        if i%12 == 0 and i!=0: time = time+18    
        else: time = time+1.5
        onset_time.append(time)
    #print(onset_time)
    matrix_list.append(onset_time)  
    
    matrix_list = np.array(matrix_list, float)
    return matrix_list				

def main():
	matrix_list = make_matrix_list()
	matrix_index = ['blockID','trial','f_imageID','s_imageID','target_ness', 'onset_time']
	save_dir = sys.argv[1]
	save_name = sys.argv[2]
	save_name = '2-%s_matrix.csv'%save_name

	make_matrix_file(matrix_list, matrix_index, save_dir, save_name)
if __name__ == '__main__':	
	main()
