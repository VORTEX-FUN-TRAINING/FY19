import os
import yaml


class OmikujiPropertiesFromYaml:

    def __init__(self):
        self.srcfile = os.path.dirname(__file__) + "/OmikujiData.yml"

    def get_omikuji_raw_data(self):
        with open(self.srcfile, 'r') as f:
            omikuji_raw_data = yaml.load(f, Loader=yaml.FullLoader)
        return omikuji_raw_data


if __name__ == '__main__':
    omkj = OmikujiPropertiesFromYaml()
    print(omkj.get_omikuji_raw_data())
