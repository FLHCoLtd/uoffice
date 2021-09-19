import json
import unittest
from uoffice.apis import EchoHandler


class TestEchoHandler(unittest.TestCase):

    def test_http_get(self):
        target = EchoHandler()
        self.assertTrue(json.loads(target.get().content).get('echo'))


if __name__ == '__main__':
    unittest.main()
