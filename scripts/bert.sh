#!/bin/bash
ZEROMQ_SOCK_TMP_DIR=/tmp/ bert-serving-start -model_dir ./chinese_L-12_H-768_A-12 -num_worker=1
