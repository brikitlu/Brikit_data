import os
import json
import jieba
import random
import argparse
import fasttext
from tqdm.auto import tqdm
from multiprocessing import Pool
import pandas as pd
import yaml

jieba.setLogLevel(20)

stopwords = set([x.strip() for x in open(
    "tasks/FastText/cn_stopwords.txt").readlines()])


def build(text):
    segs = jieba.lcut(text)
    segs = [x for x in segs if len(x) > 1 and x not in stopwords]
    return " ".join(segs)


def predict(args):
    input_path,output_path, model_path = args
    model = fasttext.load_model(model_path)
    lines = []
    with open(input_path, 'r', encoding='utf-8') as r_f:
        for line in r_f:
            lines.append(json.loads(line))

    # print("jieba cutting...")d
    seg_texts = [build(''.join(line["raw_content"])) for line in lines]

    # print("predicting...")
    labels, values = model.predict(seg_texts)

    # print("writing...")
    with open(output_path, 'w', encoding='utf-8') as w_f:
        for label, value, line in zip(labels, values, lines):
            _label = label[0].replace("__label__", "")
            _value = value[0] if value[0] <= 1 else 1
            line['fasttext_value'] = float(_value) if _label == 'clean' else float(1 - _value)

            w_f.write(json.dumps(line, ensure_ascii=False) + '\n')

class FastTextEvaluate():
    def __init__(self,config,options) -> None:
        self.config = config
        self.options = options
    
    def fasttext_evaluate(self):
        print('FastText')

        with open("config/fasttext_config.yaml", "r") as config_file:
            config = yaml.safe_load(config_file)

        input_path = config['input_path']
        output_path = config["output_path"]
        model_path = config['model_path']
        number = config["number"]
        tasks = [(input_path,output_path,model_path)]
      

        with Pool(number) as p:
                for _ in tqdm(p.imap_unordered(predict, tasks),total=len(tasks)):
                    pass
        print("运行成功")

