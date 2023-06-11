import pandas as pd
import numpy as np

class Librarian:
    def __init__(self, simulation_csv_path, qoptions_csv_path):
        self.simulation_csv_path = simulation_csv_path
        self.qoptions_csv_path = qoptions_csv_path

    def find_closest_index(self, **target_params):
        min_distance = np.inf
        closest_index = None

        chunksize = 10 ** 6  # adjust this value based on your memory capacity
        for chunk in pd.read_csv(self.csv_file, chunksize=chunksize):
            distances = np.sqrt(sum((chunk[col] - target)**2 for col, target in target_params.items()))
            min_distance_chunk = distances.min()
            if min_distance_chunk < min_distance:
                min_distance = min_distance_chunk
                closest_index = distances.idxmin()

        return closest_index
    
    def get_ith_row(self, i):
        """
        
        """
        if i < 0:  # negative indices are not allowed
            raise ValueError("Row index cannot be negative.")

        # skipping first i-1 rows, reading one row, and skipping the rest
        skip = lambda x: x < i or x > i

        try:
            row = pd.read_csv(self.qoptions_csv_path, skiprows=skip, nrows=1)
        except pd.errors.EmptyDataError:  # if the row doesn't exist
            print(f"There is no row with index {i} in the file.")
            return None

        return row
