import os.path as osp
import time
import sys
sys.path.append("/data/lz/GitHub/PubTabNet/src")
from metric import TEDS
import pprint
import json
with open("/data/lz/GitHub/OpenNMT-py/table2html/tgt-test.txt", "r") as f:
    val = f.readlines()

with open("/data/lz/GitHub/OpenNMT-py/table2html/pred_v2.txt", "r") as f:
    pred = f.readlines()

with open("/data/lz/GitHub/OpenNMT-py/table2html/src-test.txt", "r") as f:
    lines = f.readlines()

# Initialize TEDS object
teds = TEDS(n_jobs=60)


length = len(pred)
right_pred = 0
gts = {}
preds = {}

# result_teds = open("result_result.list.csv", "w")

for gt, pre, name in zip(val, pred, lines):
    # Evaluate
    gt = "<html><body><table>" + gt.strip ("\n").replace(" ", "") + "</table></body></html>"
    pre = "<html><body><table>" + pre.strip("\n").replace(" ", "") + "</table></body></html>"
    
    name = name.strip()

    gts[name] = gt
    preds[name] = {'html':pre}

    # score = teds.evaluate(pre, gt)
    # print(f'{name.strip()} TEDS score: {score*100:.2f}')
    # result_teds.write(f"{name.strip()},{score*100:.2f}\n")
    if gt == pre:
        right_pred += 1 

# Evaluate
scores = teds.batch_evaluate(gts, preds)
# Print results
pp = pprint.PrettyPrinter()
pp.pprint(scores)

acc = []

for name, pre in zip(lines, pred):
    name = name.strip("\n")
    pre = "<html><body><table>" + pre.strip("\n").replace(" ", "") + "</table></body></html>"
    score = scores[name]
    acc.append(score)
    scores[name] = {
        "score":score,
        "html":pre,
    }

    with open(f"html/{name}.md", "w") as f:
        f.write(pre)

print("acc", sum(acc)/len(acc))

with open("resultin2text_v2.json", "w") as f:
    json.dump(scores, f)


print(right_pred, length, right_pred / length * 100)