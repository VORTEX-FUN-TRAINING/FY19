import os
import unittest
from unittest.mock import MagicMock, patch

from omkjmodules.OmikujiWriter import OmikujiWriter
from omkjmodules.OmikujiProperties import OmikujiProperties


class TestOmikujiWriter(unittest.TestCase):

    def setUp(self):
        self.omkjp = OmikujiProperties()

        mocked_raw_data = {
            'daikichi':
                {'kinun':
                     {'contents': ['持ち主不明の2億円を拾う'], 'name': '金運'},
                 'unsei': '大吉',
                 'rate': 5,
                 'shigotoun': {'contents': ['他人の手柄で評価アップ'], 'name': '仕事運'},
                 'tenkyoun': {'contents': ['ステキな出会いがある'], 'name': '旅行運'}
                 }
        }

        self.omkjp.get_omikuji_raw_data = MagicMock(return_value=mocked_raw_data)
        self.omkjw = OmikujiWriter(self.omkjp)
        self.omikuji_objects = self.omkjw.get_omikuji_object_list()

    def test_get_omikuji_list(self):
        expect = {'index': 'daikichi', 'unsei': '大吉', 'rate': 5, 'kinun': '金運,持ち主不明の2億円を拾う',
                  'tenkyoun': '旅行運,ステキな出会いがある',
                  'shigotoun': '仕事運,他人の手柄で評価アップ'}

        self.assertDictEqual(vars(self.omikuji_objects[0]), expect)

    def test_get_rate(self):
        self.assertEqual(self.omikuji_objects[0].get_rate(), 5)


if __name__ == '__main__':
    unittest.main()
