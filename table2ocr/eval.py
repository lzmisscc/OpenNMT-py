import os.path as osp
import pprint
import json
from string_distance.edit_distance import levenshtein
import time
import tqdm
import logging
logging.basicConfig(
    filename='eval_log.lz.log', filemode='w',level=logging.INFO
)
class Ev:
    def __init__(self) -> None:
        self.max_length = 0
        self.max_distance = 0

        self.max_seq = 0
        self.max_right_seq = 0

    def count(self, x, y):
        cost = levenshtein(x, y)
        self.max_distance += cost
        self.max_length += max(len(x), len(y))
        if x == y:
            self.max_right_seq += 1
        self.max_seq += 1
        return cost

    def socre(self, ):
        char_acc = 1 - self.max_distance / self.max_length
        seq_acc = self.max_right_seq / self.max_seq
        return dict(char_acc=char_acc, seq_acc=seq_acc, max_seq=self.max_seq, max_right_seq=self.max_right_seq, max_distance=self.max_distance, max_length=self.max_length)

ev = Ev()
  
with open("/data/lz/GitHub/OpenNMT-py/table2ocr/tgt-test", "r") as f:
    val = f.readlines()

with open("/data/lz/GitHub/OpenNMT-py/table2ocr/pred_v2.txt", "r") as f:
    pred = f.readlines()

with open("/data/lz/GitHub/OpenNMT-py/table2ocr/src-test", "r") as f:
    lines = f.readlines()




length = len(pred)
right_pred = 0
gts = {}
preds = {}

td = tqdm.tqdm(zip(val, pred, lines))

for gt, pre, name in td:
    # Evaluate
    gt = ''.join(gt.strip().split(" ")).replace('<space>', ' ')
    pre = ''.join(pre.strip().split(" ")).replace('<space>', ' ')
    
    name = name.strip()


    ev.count(gt, pre)

    socre = ev.socre()
    if gt != pre:
        logging.info(f"{name}\t{gt}")
        logging.info(f"{name}\t{pre}\n")
    td.set_description(f"char_acc:{socre['char_acc']*100:.3};seq_acc:{socre['seq_acc']*100:.3f}")
