import os
import re

import tqdm

html_label = ['<b>', '</b>', '<i>', '</i>', '<sup>', '</sup>', '<sub>', '</sub>',
'<underline>', '</underline>', '<space>']
def split_fileanme_content(line):
    name, token = line.strip().replace(' ', '<space>').split('\t', )
    # token = re.split('(<.*?>)', token) # 正则算法修复
    token = re.split('(<[^<^>^0-9]+?>)', token) # 正则算法修复
    if token and token[0] == '':
        token.pop(0)
    if token and token[-1] == '':
        token.pop(-1)
    new_token = []
    for t in token:
        new_token += [t] if t in html_label else list(t)
    return name.replace('\\', '/')+ '\n', ' '.join(new_token) + '\n'

# res = split_fileanme_content("das.jpg\t<<b><<=>daa sada</b>")
# exit(res)

# 训练集
with open('data_v2/train-300w.txt', 'r') as f:
    lines = f.readlines()


names, tokens = [], []
lines = tqdm.tqdm(lines)

for l in lines:
    name, token = split_fileanme_content(l)
    names.append(name)
    tokens.append(token)
with open('src-train', 'w') as f:
    f.writelines(names)
with open('tgt-train', 'w') as f:
    f.writelines(tokens)


# 验证集
with open('data_v2/val.txt', 'r') as f:
    lines = f.readlines()
names, tokens = [], []
lines = tqdm.tqdm(lines)

for l in lines:
    name, token = split_fileanme_content(l)
    names.append(name)
    tokens.append(token)

with open('src-val', 'w') as f:
    f.writelines(names)
with open('tgt-val', 'w') as f:
    f.writelines(tokens)

with open('src-test', 'w') as f:
    f.writelines(names)
with open('tgt-test', 'w') as f:
    f.writelines(tokens)
