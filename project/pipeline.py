import os
import requests
import zipfile
import pandas as pd

#education & economy
url = [
    "https://api.worldbank.org/v2/en/indicator/SE.PRM.ENRR?downloadformat=csv",
    "https://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.CD?downloadformat=csv"
    ]

data = [
    os.path.join("./data/data1.zip"),
    os.path.join("./data/data2.zip")
]

csv_dir = [
    os.path.join("./data/data1.csv"),
    os.path.join("./data/data2.csv")
]

#Download and save data
try:
    for i in range(2):
        response = requests.get(url[i])
        response.raise_for_status()

        with open(data[i], "wb") as f:
            f.write(response.content)
        print("Zip File {} saved".format(i+1))

        # Extract csv from zip
        with zipfile.ZipFile(data[i], "r") as file:
            csv = file.namelist()[1]
            file.extract(csv, "./data")
            os.rename(os.path.join("./data", csv), csv_dir[i])
            # pd.read_csv(csv_dir[i], skiprows=2).to_csv(csv_dir[i])
        
        os.remove(data[i])

except Exception as e:
    print(e)
    
#Clean Data
try:
    americas = [
        "United States", "Canada", "Mexico", "Guatemala", "Honduras", "Costa Rica", "Brazil", "Argentina", "Colombia", "Chile"
    ]
    cols = ["Country Name", "Country Code"] + [str(i) for i in range(1970, 2024)]

    for i in range(2):
        df = pd.read_csv(csv_dir[i], skiprows=4, header=0)
        # print(df.head())
        df = df[cols]
        df = df[df["Country Name"].isin(americas)]
        df = df.infer_objects()
        # df.update(df.select_dtypes(include=['float64', 'int64']).interpolate(method='linear'))
        df.loc[:, [str(i) for i in range(1970, 2024)]] = df.loc[:, [str(i) for i in range(1970, 2024)]].fillna(df.loc[:, [str(i) for i in range(1970, 2024)]].mean())
        print(df)
        df.to_csv(csv_dir[i])
        print("Data {} extracted".format(i+1))

except Exception as e:
    print("Exception raised\n\n",e)
        
