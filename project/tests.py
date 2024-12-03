import os
import unittest
import pandas as pd
from pipeline import download_data, extract_data, clean_data, pipeline, get_path
from tabulate import tabulate

class TestPipeline(unittest.TestCase):

    data_dir = "./data"
    test_url = "https://api.worldbank.org/v2/en/indicator/SE.PRM.ENRR?downloadformat=csv"
    test_filename = "test_data"

    @classmethod
    def setUpClass(cls):
        # Ensure the data directory exists
        os.makedirs(cls.data_dir, exist_ok=True)

    def tearDown(self):
        # Cleanup any files created during testing
        for ext in ["zip", "csv"]:
            file_path = get_path(self.test_filename, ext)
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_download_data(self):
        """Test if data is downloaded and saved as a zip file."""
        download_data(self.test_url, self.test_filename)
        zip_path = get_path(self.test_filename, "zip")
        self.assertTrue(os.path.exists(zip_path), "Zip file was not created")

    def test_extract_data(self):
        """Test if data is extracted correctly."""
        download_data(self.test_url, self.test_filename)
        extract_data(self.test_filename)
        csv_path = get_path(self.test_filename, "csv")
        self.assertTrue(os.path.exists(csv_path), "CSV file was not extracted")

    def test_clean_data(self):
        """Test if data is cleaned and saved correctly."""
        download_data(self.test_url, self.test_filename)
        extract_data(self.test_filename)
        clean_data(self.test_filename)
        csv_path = get_path(self.test_filename, "csv")
        self.assertTrue(os.path.exists(csv_path), "Cleaned CSV file was not saved")
        
        # Check content
        df = pd.read_csv(csv_path)
        self.assertIn("United States", df["Country Name"].values, "Expected countries not found in the cleaned data")
        self.assertFalse(df.isnull().any().any(), "Cleaned data contains NaN values")

    def test_pipeline(self):
        """Test the entire pipeline."""
        pipeline(self.test_url, self.test_filename)
        csv_path = get_path(self.test_filename, "csv")
        self.assertTrue(os.path.exists(csv_path), "Pipeline did not produce a cleaned CSV file")

if __name__ == "__main__":
    loader = unittest.TestLoader()
    test_results = {}
    tests = loader.loadTestsFromTestCase(TestPipeline)
    total_tests = 0
    passed_tests = 0

    # Run each test and store the result
    for i, test in enumerate(tests, 1):
        result = unittest.TextTestRunner().run(unittest.TestSuite([test])).wasSuccessful()
        if result:
            test_results[test._testMethodName] = "OK"
            passed_tests += 1
        else:
            test_results[test._testMethodName] = "FAIL"
        total_tests += 1

    # Print results in tabulated form
    print("============= Test Results ==============")
    table = [[i, test_name, outcome] for i, (test_name, outcome) in enumerate(test_results.items(), 1)]
    table.append(["", "Total Tests Passed", f"{passed_tests} / {total_tests}"])
    print(tabulate(table, headers=['Pos', 'Test Case', 'Result'], tablefmt="github"))

