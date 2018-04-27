import unittest
from nbu_cmd.common import run_cmd

class CmdTestCase(unittest.TestCase):
    def test_run(self):
        result = run_cmd('ls /home')
        self.assertEqual(type(result),str)

if __name__ == '__main__':
    unittest.main()
