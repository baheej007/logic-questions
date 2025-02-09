import multiprocessing
import pandas as pd

def process_chunk(chunk):
    result = chunk[chunk["price"] > 100]  # Filter expensive items
    return result

if __name__ == "__main__":
    df = pd.read_csv("large_dataset.csv", chunksize=10000)  # Read in chunks
    with multiprocessing.Pool() as pool:
        results = pool.map(process_chunk, df)
    
    final_df = pd.concat(results)
    final_df.to_csv("filtered_data.csv", index=False)