import os
import unittest
from unittest.mock import MagicMock, patch

from omkjmodules.OmikujiPropertiesFromYaml import OmikujiPropertiesFromYaml


class TestOmikujiPropertiesFromYaml(unittest.TestCase):
    def setUp(self) -> None:
        self.target = OmikujiPropertiesFromYaml()
        self.target.srcfile = os.path.dirname(__file__) + "/TestOmikujiData.yml"

    def test_get_omikuji_raw_data(self):
        expect = {
            'daikichi':
                {'kinun':
                     {'contents': ['持ち主不明の2億円を拾う'], 'name': '金運'},
                 'unsei': '大吉',
                 'rate': 5,
                 'shigotoun': {'contents': ['他人の手柄で評価アップ'], 'name': '仕事運'},
                 'tenkyoun': {'contents': ['ステキな出会いがある'], 'name': '旅行運'}
                 }
        }

        result = self.target.get_omikuji_raw_data()
        self.assertDictEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
