import jsonlines



class AverageRotation():
    def __init__(self,config,options) -> None:
        self.config = config
        self.options = options
    
    def average_rotation(self):
        print('analysis......')
        file_path = 'data/input_data/average_rounds_data.jsonl'  # JSONL文件路径
        total_texts = []  # 存储所有文本
        with jsonlines.open(file_path) as reader:
            for line in reader:
                text = line['text']  # 假设JSONL中的文本字段名为'text'
                total_texts.append(text)
        # 计算平均轮次（以换行符为例）
        total_rounds = sum(text.count('\n') for text in total_texts) / len(total_texts)
        print(f"Average Rounds in texts: {total_rounds}")



