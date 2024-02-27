from text_cleaner import DataCleaner
# safe importing of main module in multi-processing
if __name__ == "__main__": 
    # you need to specify your own configuration file path
    cleaner = DataCleaner("./config/config.yaml")
    cleaner.clean()
