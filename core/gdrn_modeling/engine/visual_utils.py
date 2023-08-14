import os.path as osp
import pickle
from pprint import pprint
# import ref

def run_file():
    data_directory = "/home/fabrice//Documents/gdrnpp/gdrnpp_bop2022_f1/output/gdrn/tless/convnext_a6_AugCosyAAEGray_BG05_mlL1_DMask_amodalClipBox_classAware_tless/pose_results_epoch_9_iter_159288/tless_bop_test_primesense/pred_pose_and_inputs_idx_72.pkl"
    data_dict = {}

    with open(data_directory, 'rb') as results:         # open the results.pkl file 
        data_dict = pickle.load(results)                # and save the data in data_dict

    img_ids = list(data_dict["inputs"][0]["file_name"])                    # get the keys of the data_dict
    out_dict = data_dict["outputs"]["trans"]
    pprint(img_ids)
    # print(len(out_dict))


    
    # for idx, obj_data in enumerate(data_dict['1/1']):   # get each object's data separately
    #     if (idx != 0): 
    #         break
        


if __name__ == '__main__':
    run_file()