from pathlib import Path
import fasttext  # type: ignore
from typing import Dict, Optional
from tasks.language_identification import jsonql
from tasks.language_identification import split_by_lang
from tasks.language_identification.split_by_lang import Classifier



class LanguageIdentification():
    def __init__(self,config,options) -> None:
        self.config = config
        self.options = options

    def language_identification(self):
        print("language identification")
        model = Path("./data/models/FastText/lid.176.bin")

        classifier = Classifier(model, "text", "lang")
        classifier.__enter__()
        doc_zh = dict(text="面向大模型研究领域的高效易用数据处理工貝包")
        doc_en = dict(text="Efficient and Easy-to-Use Data Processing Workbags for Large Modeling Research Domain")
        doc_ru = dict(
            text="Эффективные и простые в использовании рабочие пакеты для обработки данных в области исследования больших моделей")
        doc_fr = dict(
            text="Sacs de travail efficaces et faciles à utiliser pour le traitement des données dans le domaine de la recherche sur les grands modèles")
        doc_de = dict(
            text="Effiziente und einfach zu verwendende Datenverarbeitungs-Workbags für große Modellforschungsbereiche")
        doc_ja = dict(text="大規模モデル研究領域のための効率的で使いやすいデータ処理ワークバッグ")
        results_zh = classifier(doc_zh)
        results_en = classifier(doc_en)
        results_ru = classifier(doc_ru)
        results_fr = classifier(doc_fr)
        results_de = classifier(doc_de)
        results_ja = classifier(doc_ja)
        print(
            f"language type: {results_zh.get('lang')}, language source:{results_zh.get('lang_score')} , original text: {results_zh.get('text')} .")
        print(
            f"language type: {results_en.get('lang')}, language source:{results_en.get('lang_score')} , original text: {results_en.get('text')} .")
        print(
            f"language type: {results_ru.get('lang')}, language source:{results_ru.get('lang_score')} , original text: {results_ru.get('text')} .")
        print(
            f"language type: {results_fr.get('lang')}, language source:{results_fr.get('lang_score')} , original text: {results_fr.get('text')} .")
        print(
            f"language type: {results_de.get('lang')}, language source:{results_de.get('lang_score')} , original text: {results_de.get('text')} .")
        print(
            f"language type: {results_ja.get('lang')}, language source:{results_ja.get('lang_score')} , original text: {results_ja.get('text')} .")
        
