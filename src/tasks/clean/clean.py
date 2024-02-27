class Clean():
    def __init__(self,config,options) -> None:
        self.config = config
        self.options = options
    
    def clean(self):
        from tasks.clean.text_cleaner import DataCleaner
        cleaner = DataCleaner("config/clean_config.yaml")
        # import ipdb
        # ipdb.set_trace()
        cleaner.clean()
        print("end clean!")