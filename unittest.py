def test_flake8_linting(self):
    result = !flake8 "C:/DEV/pipelines/NewTest"
    self.assertEqual(result, "", "There are linting errors")
    