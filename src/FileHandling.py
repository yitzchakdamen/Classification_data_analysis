import pandas as pd
import json 
import os

class FileHandling:
    
    def __init__(self, source_file_directory:str, destination_file_directory:str) -> None:
        pass
    
    def upload_data_file(self, file_name: str) -> pd.DataFrame:
        pass 
    
    def saving_data_file(self, file_name: str, data:pd.DataFrame) -> None:
        pass
    
    def saving_results_json(self, file_name: str, results:dict) -> None:
        os.makedirs(dir_fils, exist_ok=True)
        with open(file= os.path.join(dir_fils, f"{file_name}.json") , mode="w", encoding="utf-8") as file:
            json.dump(obj=model, fp=file, indent=4)
