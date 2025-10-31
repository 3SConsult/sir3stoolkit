import unittest

class BasicImportTest(unittest.TestCase):
    def test_package_import(self):
        try:
            import sir3stoolkit  
        except ImportError as e:
            self.fail(f"Import failed: {e}")
        try:
            from sir3stoolkit.core import wrapper
            from sir3stoolkit.mantle   import dataframes
            from sir3stoolkit.mantle import alternative_models
            from sir3stoolkit.mantle import mantle
        except Exception as e:
            self.fail(f"Import failed: {e}")

if __name__ == "__main__":
    unittest.main()