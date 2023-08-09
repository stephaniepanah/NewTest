def test_flake8_linting(self):
    result = !flake8 "C:/DEV/JenkinsTest/jenkins"
    self.assertEqual(result, "", "There are linting errors")
    