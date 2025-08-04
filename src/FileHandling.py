import pandas as pd
import json 
import os

class FileHandling:
    
    def __init__(self, source_file_directory:str, destination_file_directory:str) -> None:
        self.source_file_directory = source_file_directory
        self.destination_file_directory = destination_file_directory
    
    def upload_data_file(self, file_name: str) -> pd.DataFrame:
        os.makedirs(self.source_file_directory, exist_ok=True)
        file = os.path.join(self.source_file_directory, file_name)
        return pd.read_csv(file)
    
    def saving_data_file(self, file_name: str, data:pd.DataFrame) -> None:
        os.makedirs(self.destination_file_directory, exist_ok=True)
        file = os.path.join(self.destination_file_directory, f"{file_name}.csv")
        data.to_csv(file, index=False)
            
    def saving_results_json(self, file_name: str, results:dict) -> None:
        os.makedirs(self.destination_file_directory, exist_ok=True)
        
        with open(file= os.path.join(self.destination_file_directory, f"{file_name}.json") , mode="w", encoding="utf-8") as file:
            json.dump(obj=results, fp=file, indent=4)



    