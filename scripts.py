# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:00:22 2021

scripts for training, validating and testing

@author: qia011
"""


# =========== training command for yolov5
# --cfg # model configuration 
# -- weights # pre-trained model weights
# -- hyp # training hyper-parameters
# -- data # data information, categories, training & testing 
# -- img-size # 
# -- project # output folder names, 
# coco128 - with pre-trained model
# coco128_scratch - without pre-trained model
# Bayescoco128 - with bayesian model
# =======================

python3 -W ignore train.py \
--batch-size 40 \
--epochs 300 \
--cfg models/yolov5s_coco128.yaml \
--weights '' \
--hyp data/hyp.scratch.yaml \
--data data/coco128.yaml \
--img-size 640 \
--project runs/coco128_scratch 




# =========== training command for bayesian yolov5
# --cfg # model configuration 
# -- weights # pre-trained model weights
# -- hyp # training hyper-parameters
# --beta # kl loss 
# -- data # data information, categories, training & testing 
# -- img-size # 
# -- project # output folder names, coco128 or Bayescoco128
# =======================

python3 -W ignore BBBtrain.py \
--batch-size 40 \
--epochs 300 \
--cfg models/yolov5s_coco128.yaml \
--weights '' \
--hyp data/hyp.scratch.yaml \
--beta 0.1\
--data data/coco128.yaml \
--img-size 640 \
--project runs/Bayescoco128 
