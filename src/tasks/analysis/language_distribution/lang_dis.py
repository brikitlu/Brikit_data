import jsonlines
from pathlib import Path
from tasks.analysis.language_distribution.split_by_lang import Classifier
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go

class LanguageDistribution():
    def __init__(self,config,options) -> None:
        self.config = config
        self.options = options
    
    def language_distribution(self):
        print('analysis......')
        file_path = 'data/input_data/language_distribution_data.jsonl'  # JSONL文件路径
        languages_count = {}  # 用于存储每种语言的出现次数
        model = Path( "data/models/FastText/lid.176.bin")
        classifier = Classifier(model, "text", "lang")
        classifier.__enter__()
        with jsonlines.open(file_path) as reader:
            for line in reader:
                text = line['text']  # 假设JSONL中的文本字段名为'text'
                try:
                    language = classifier(dict(text=text)).get('lang')  # 使用语言检测库进行语言识别
                    if language in languages_count:
                        languages_count[language] += 1
                    else:
                        languages_count[language] = 1
                except:
                    pass  # 忽略无法识别语言的文本行
        # 输出每种语言的出现次数
        languages = []        
        for lang, count in languages_count.items():
            print(f"Language: {lang}, Count: {count}")
            languages.append(lang)
        # 将语言和对应的频率数据转换为列表，方便绘图
        print(languages)
        counts = list(languages_count.values())
        # 为展示效果，使用如下数据，具体使用时，需要用languages、counts替换labels和values_pie、values_bar
        fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'bar'}]])
        fig.add_trace(go.Pie(labels=languages, values=counts, name="Language Distribution"), row=1, col=1)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(title_text="Language Distribution")
        fig.add_trace(go.Bar(x=languages, y=counts ), row=1, col=2)
        fig.show()
