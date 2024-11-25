import os
import requests
import zipfile
import pandas as pd

data_dir = "./data"
os.makedirs(data_dir, exist_ok=True)

def get_path(filename, ext):
    return os.path.join(data_dir, f"{filename}.{ext}")

#Download and save data
def download_data(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = get_path(filename, "zip")
        with open(data, "wb") as f:
            f.write(response.content)
        print("Zip File saved")

    except Exception as e:
        print(e)

def extract_data(filename):
    data = get_path(filename, "zip")
    try:
        csv_dir = get_path(filename, "csv")
        with zipfile.ZipFile(data, "r") as file:
            csv = file.namelist()[1]
            file.extract(csv, "./data")
            os.rename(os.path.join("./data", csv), csv_dir)
        
        os.remove(data)
    except Exception as e:
        print(e)
    
#Clean Data
def clean_data(filename):
    americas = [
            "United States", "Canada", "Mexico", "Guatemala", "Honduras", "Costa Rica", "Brazil", "Argentina", "Colombia", "Chile"
        ]
    cols = ["Country Name", "Country Code"] + [str(i) for i in range(1970, 2024)]
    try:
        csv_dir = get_path(filename, "csv")

        df = pd.read_csv(csv_dir, skiprows=4, header=0)
        df = df[cols]
        df = df[df["Country Name"].isin(americas)]

        df = df.infer_objects()
        df.loc[:, [str(i) for i in range(1970, 2024)]] = df.loc[:, [str(i) for i in range(1970, 2024)]].fillna(df.loc[:, [str(i) for i in range(1970, 2024)]].mean())
        
        df.to_csv(csv_dir)
        print("Data extracted")

    except Exception as e:
        print("Exception raised\n\n",e)

def combine_file(filenames):
    df = []
    try:
        for filename in filenames:
            file = get_path(filename, "csv")
            df.append(pd.read_csv(file))
        
        combined_df = df[0]
        for df in df[1:]:
            combined_df = pd.merge(combined_df, df, on="Country Name", how="inner", suffixes=('', '_other'))

        combined_file_path = get_path("combined_data", "csv")
        combined_df.to_csv(combined_file_path, index=False)
        print(f"Combined file saved at {combined_file_path}")
        
    
    except Exception as e:
        print("Exception raised\n\n",e)


def pipeline(url, filename):
    download_data(url, filename)
    extract_data(filename)
    clean_data(filename)


#education & economy
data_url = [
    "https://api.worldbank.org/v2/en/indicator/SE.PRM.ENRR?downloadformat=csv",
    "https://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.CD?downloadformat=csv",
]

pipeline(data_url[0], "data1")
pipeline(data_url[1], "data2")
combine_file(["data1", "data2"])

