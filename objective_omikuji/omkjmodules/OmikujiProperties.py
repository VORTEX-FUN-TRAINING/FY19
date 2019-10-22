from .OmikujiPropertiesFromYaml import OmikujiPropertiesFromYaml


class OmikujiProperties(OmikujiPropertiesFromYaml):

    def __init__(self):
        super().__init__()

    def get_omikuji_raw_data(self):
        return super().get_omikuji_raw_data()


if __name__ == '__main__':
    omkjp = OmikujiProperties()
    print(omkjp.get_omikuji_raw_data())
