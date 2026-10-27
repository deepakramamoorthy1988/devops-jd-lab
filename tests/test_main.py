import unittest

from app.main import get_status


class TestApplication(unittest.TestCase):

    def test_application_status(self):
        result = get_status()

        self.assertEqual(result["application"], "devops-jd-lab")
        self.assertEqual(result["status"], "healthy")
        self.assertEqual(result["version"], "1.0.0")


if __name__ == "__main__":
    unittest.main()