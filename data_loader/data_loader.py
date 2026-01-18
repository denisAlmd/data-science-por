import pandas as pd

class DataLoader:


    def load_data(self, path: str) -> pd.DataFrame:
        path_extension = path.split('.')[-1].lower()
        data = pd.DataFrame()
        try:
            match path_extension:
                case 'csv':        
                    data = pd.read_csv(path)
                    return data 
                case 'xlsx':
                    data = pd.read_excel(path)
                    return data
                case 'json':
                    data = pd.read_json(path)
                    return data
        except Exception as e:
            print(f"Error loading data from {path}: {e}")     
        return data
        