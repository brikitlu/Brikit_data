import common.command_line as command_line


def dispatch(config, options, actions):
    '''
    ##  路由命令分发
    * 分支节点会执行节点下的 run 子节点的函数
    * 叶子节点直接执行对应函数
    python main.py -a tasks.xxx.xxx
    
    其中
    * xxx 是 tasks/xxx/ 目录下任意名为 xxx(config, options) 的函数
    * 在tasks/xxx/__init__.py: dispatch()方法里需要注册需要被识别的模块

    '''
    command_line.dispatch(config, options, actions, {
        'test': lambda: task_test(config, options),
        'clean':lambda: task_clean(config, options),
        'lid':lambda: task_language_identififcation(config, options),
        'evaluate_bert':lambda: task_bert_evaluate(config, options),
        'evaluate_fasttext':lambda: task_fasttext_evaluate(config, options),
        'text_dedup':lambda: task_dedup(config, options),
        'pdf_transform':lambda: task_pdf_transform(config, options),
        'equb_transform':lambda: task_equb_transform(config, options),
        'average_rotation':lambda: task_average_rotaition(config, options),
        'text_length':lambda: task_text_length(config, options),
        'language_distribution':lambda: task_language_distribution(config, options)
    })
    
def task_test(config, options):
    from tasks.test.test import TestHello
    task = TestHello(config, options)
    task.test_hello()

def task_clean(config,options):
    from tasks.clean.clean import Clean
    task = Clean(config,options)
    task.clean()

def task_language_identififcation(config,options):
    from tasks.language_identification.lid import LanguageIdentification
    task = LanguageIdentification(config,options)
    task.language_identification()

def task_bert_evaluate(config,options):
    from tasks.Bert.evaluate_bert import BertEvaluate
    task = BertEvaluate(config,options)
    task.bert_evaluate()

def task_fasttext_evaluate(config,options):
    from tasks.FastText.evaluate_fasttext import FastTextEvaluate
    task = FastTextEvaluate(config,options)
    task.fasttext_evaluate()    

def task_dedup(config,options):
    from tasks.text_dedup.start_dedup import Deduplicating
    task = Deduplicating(config,options)
    task.start_dedup()  

def task_pdf_transform(config,options):
    from tasks.all2txt.pdf_transform import TransformPDF
    task = TransformPDF(config,options)
    task.pdf_transform()

def task_equb_transform(config,options):
    from tasks.all2txt.epub_transform import TransformEqub
    task = TransformEqub(config,options)
    task.equb_transform()

def task_average_rotaition(config,options):
    from tasks.analysis.average_rotation_analysis import AverageRotation
    task = AverageRotation(config,options)
    task.average_rotation()


def task_text_length(config,options):
    from tasks.analysis.text_length_analysis import TextLength
    task = TextLength(config,options)
    task.text_length()

def task_language_distribution(config,options):
    from tasks.analysis.language_distribution.lang_dis import LanguageDistribution
    task = LanguageDistribution(config,options)
    task.language_distribution()