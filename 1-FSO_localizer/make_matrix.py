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
    num_target = [1,2,2,2,3]
    #target = random.sample(range(1,11),random.choice(num_target))
    
    target = random.sample(range(1,11),target_count)
    
    if len(target) == 2:
      if abs(target[0]-target[1]) > 1:
        return target
        break
    elif len(target) == 3:
      if abs(target[0]-target[1]) > 1 and abs(target[0]-target[2]) > 1 and abs(target[1]-target[2]) > 1:
        return target
        break
    else:
      return target
      break

def make_target_count():   
    target_count = [1,1,1,1]
    add_1 = random.sample([0,1,2,3], 2 )
    add_2 = random.sample([0,1,2,3], 2 )
    
    target_count[add_1[0]] += 1 
    target_count[add_1[1]] += 1 
    
    target_count[add_2[0]] += 1 
    target_count[add_2[1]] += 1

    return target_count

def make_matrix_list():
    matrix_list = []
    #print("==BlockID ==")

    blockID = []
    blockID_list = [i+1 for i in range(12)]
    for i in range(len(blockID_list)):
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

    #print("== Category ==")
    category = []
    category_list = []
    for i in range(4): category_list.append(1)
    for i in range(4): category_list.append(2)
    for i in range(4): category_list.append(3)
    random.shuffle(category_list)
    for i in range(12):
        for j in range(12):
            category.append(category_list[i])
    #print(category)
    matrix_list.append(category)

    #print("=======ImageID=======")
    imageID=[]
    f_img_idx = [i+1 for i in range(48)]
    s_img_idx = [i+1 for i in range(48)]
    o_img_idx = [i+1 for i in range(48)]
    np.random.shuffle(f_img_idx)
    np.random.shuffle(s_img_idx)
    np.random.shuffle(o_img_idx)
    for i in range(3):
        for j in range(48):
            idx = i*48+j 
            if category[idx] == 1:
                img=f_img_idx[0]
                del f_img_idx[0]
                imageID.append(img)
            elif category[idx] == 2:
                img=s_img_idx[0]
                del s_img_idx[0]
                imageID.append(img)
            elif category[idx] == 3:
                img=o_img_idx[0]
                del o_img_idx[0]
                imageID.append(img)

    # Condition (Do Not Repeat Same Image!)
    for i in range(48):
        cond = imageID.count(i+1)
        if cond!=3:
            print("Condition did not satisfied")
            exit()

    #print(imageID)    
    matrix_list.append(imageID)

    #print("=======Target-ness=======")
    target_ness = []
    target_list = [[] for i in range(12)] 
    
    f_target_count = make_target_count()
    f_block_idx = np.where(np.array(category_list)==1)[0]
    for i in range(4): 
        target = select_random_number(f_target_count[i])
        target_list[f_block_idx[i]] = target

    s_target_count = make_target_count()
    s_block_idx = np.where(np.array(category_list)==2)[0]
    for i in range(4): 
        target = select_random_number(s_target_count[i])
        target_list[s_block_idx[i]] = target
    
    o_target_count = make_target_count()
    o_block_idx = np.where(np.array(category_list)==3)[0]
    for i in range(4): 
        target = select_random_number(o_target_count[i])
        target_list[o_block_idx[i]] = target
    
    print(f_target_count, s_target_count, o_target_count)
    print(f_block_idx, s_block_idx, o_block_idx) 
    print(target_list) 
   
    for i in range(12):
        for j in range(len(target_list)):
            if j in target_list[i]:
                target_ness.append(1)
            else: target_ness.append(0)
    #print(target_ness)
    matrix_list.append(target_ness)

    #print("=======Onset time=======")
    onset_time = []
    time = 0
    for i in range(144):
        if i%12 == 0 and i!=0: time = time+12 
        else: time = time+1.5
        onset_time.append(time)
    #print(onset_time)
    matrix_list.append(onset_time)  
    
    matrix_list = np.array(matrix_list, float)
    return matrix_list				

def main():
    matrix_list = make_matrix_list()
    matrix_index = ['blockID','trial','category','imageID','target_ness', 'onset_time']
    save_dir = sys.argv[1]
    if len(sys.argv) == 3:
        save_name = sys.argv[2]
    else:
	    save_name = '1_matrix.csv'

    make_matrix_file(matrix_list, matrix_index, save_dir, save_name)
if __name__ == '__main__':	
    main()
