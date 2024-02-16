import os
from optimazation import sim_loop
from models.networks import ContactEstimationNetwork
import argparse

import torch
if __name__ == '__main__':

 
    parser = argparse.ArgumentParser(description='arguments for predictions')
    parser.add_argument('--contact_estimation', type=int, default=0)
    parser.add_argument('--image_size',type=int, default=1024) 
    parser.add_argument('--floor_known', type=int, default=1)
    parser.add_argument('--model_path', default="models/ConStaNet_sample(1).pkl") 
    parser.add_argument('--floor_frame',  default="data/floor_frame.npy") 
    parser.add_argument('--openpose_2d_path', default="data/sample_vnect_2ds.npy") 
    parser.add_argument('--humanoid_path', default='asset/physcap.urdf') 
    parser.add_argument('--skeleton_filename', default="asset/physcap.skeleton" )
    parser.add_argument('--motion_filename', default="data/sample.motion")
    #parser.add_argument('--floor_path', default="asset/plane.urdf") 
    parser.add_argument('--contact_path', default="data/sample_contacts.npy") 
    parser.add_argument('--stationary_path', default="data/sample_stationary.npy")
    parser.add_argument('--save_path', default='./results/')
    args = parser.parse_args()

   
    ### Physics-based Optimization ###
    path_dict={ 
            "floor_frame":args.floor_frame, 
            "humanoid_path":args.humanoid_path,
            "skeleton_filename":args.skeleton_filename,
            "motion_filename":args.motion_filename,
            "floor_path":args.floor_path,
            "contact_path":args.contact_path,
            "stationary_path":args.stationary_path,
            "save_path":args.save_path} 
    print("Stage III running ... ") 
    sim_loop(path_dict,floor_known=args.floor_known)
    print("Done. Predictions were saved at "+args.save_path)
    