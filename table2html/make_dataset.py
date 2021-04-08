import jsonlines
import tqdm
from PIL import Image
import os.path as osp
Reader = jsonlines.open("/data/lz/GitHub/OpenNMT-py/pubtabnet/PubTabNet_2.0.0.jsonl", "r").iter()
Reader = tqdm.tqdm(Reader)

src_train = open("src-train.txt", "w")
tgt_train = open("tgt-train.txt", "w")
src_test = open("src-test.txt", "w")
tgt_test = open("tgt-test.txt", "w")
src_val = open("src-val.txt", "w")
tgt_val = open("tgt-val.txt", "w")
train_count = 1
test_count = 1
for line in Reader:
    filename = line['filename']
    split = line['split']
    # if split == "train":
    #     train_count += 1 
    #     if train_count >= 10000:
    #         continue
    # elif split == "val":
    #     test_count += 1
    #     if test_count >= 10000:
    #         break
    html = line['html']['structure']['tokens']
    html = " ".join(html)

    # image_path = osp.join("/data/lz/GitHub/OpenNMT-py/pubtabnet", split, filename)
    # image = Image.open(image_path)
    # image.save(f"images/{filename}")

    if split == "train":
        src_train.write(f"{filename}\n")
        tgt_train.write(f"{html}\n")
    elif split == "val":
        src_test.write(f"{filename}\n")
        tgt_test.write(f"{html}\n")
        src_val.write(f"{filename}\n")
        tgt_val.write(f"{html}\n")

