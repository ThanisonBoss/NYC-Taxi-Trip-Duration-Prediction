import wget
import argparse
import os

def download_file(year, month, destination_path):
    file_name = f"green_tripdata_{year}-{month}.parquet"
    url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/' + file_name
    if os.path.exists(destination_path + file_name):
        os.remove(destination_path + file_name)
    wget.download(url, destination_path)

def download(param):
    year, month = param.year, param.month
    destination_path = f'data/raw/{year}/'
    if not os.path.exists(destination_path):
        os.makedirs(destination_path, exist_ok=True)
    if month:
        download_file(year, month, destination_path)
    else:
        for month in range(1,13):
            month = str(month).zfill(2)
            download_file(year, month, destination_path)

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description='Download nyc taxi data')
    parser.add_argument('-y', '--year', type=str, required=True) 
    parser.add_argument('-m', '--month', type=str)

    # Parse the arguments
    args = parser.parse_args()
    download(args)