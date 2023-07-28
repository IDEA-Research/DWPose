# -*- coding: utf-8 -*-

import torch
import argparse
from collections import OrderedDict

def change_model(args):
    dis_model = torch.load(args.dis_path)
    all_name = []
    if args.two_dis:
        for name, v in dis_model["state_dict"].items():
            if name.startswith("teacher.backbone"):
                all_name.append((name[8:], v))
            elif name.startswith("student.head"):
                all_name.append((name[8:], v))
            else:
                continue
    else:
        for name, v in dis_model["state_dict"].items():
            if name.startswith("student."):
                all_name.append((name[8:], v))
            else:
                continue
    state_dict = OrderedDict(all_name)
    dis_model['state_dict'] = state_dict
    if 'optimizer' in dis_model.keys():
        dis_model.pop('optimizer')
    torch.save(dis_model, args.output_path) 

           
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Transfer CKPT')
    parser.add_argument('dis_path', type=str, default='work_dirs/dwpose_l_dis_m__coco-ubody-256x192/latest.pth', 
                        metavar='N',help='dis_model path')
    parser.add_argument('output_path', type=str, default='dw-l-m_ucoco.pth',metavar='N', 
                        help = 'output path')
    parser.add_argument('--two_dis', action='store_true', default=False, help = 'if two dis')
    args = parser.parse_args()
    change_model(args)
