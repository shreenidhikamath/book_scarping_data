import unittest
import os
import pandas as pd

class TestBookScraper(unittest.TestCase):

    def setUp(self):
        self.filename = "books_data.csv"


    def test_01_csv_file_exists(self):
        """Test Case 1: Check if CSV file exists"""
        print("books_data.csv exists:", os.path.isfile("books_data.csv"))  # Should return True

  
    def test_02_csv_file_extraction(self):
        """Test Case 2: Verify CSV File Extraction"""
        try:
            df = pd.read_csv(self.filename)
            print("\nFirst 5 rows of the dataset:\n", df.head())  
            self.assertIsInstance(df, pd.DataFrame)
        except Exception as e:
            self.fail(f"CSV extraction failed: {e}")
   
   
    def test_03_file_extension(self):
        """Test Case 3: Verify FileType and DataType"""
        df = pd.read_csv("books_data.csv")
        print("File extension:", os.path.splitext("books_data.csv")[1])  # Should return '.csv'
        print(df["Price"].dtype)  # Should be 'float'    
              

    def test_04_data_columns_match(self):
        """Test Case 4: Validate Required Columns Exist"""
        df = pd.read_csv(self.filename)
        expected_columns = ["Title", "Price", "Rating", "Availability", "Product URL"]
        print(df.columns.tolist() == expected_columns)  # Should return True

    def test_05_no_missing_values(self):
        """Test Case 5: Handle Missing or Invalid Data"""
        df = pd.read_csv(self.filename)
        print(df.isnull().sum())  # Should show zero missing values

if __name__ == '__main__':
    unittest.main()
