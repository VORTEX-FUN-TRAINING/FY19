#!/usr/bin/env python3


def main():
    from omkjmodules.OmikujiProperties import OmikujiProperties
    from omkjmodules.OmikujiWriter import OmikujiWriter
    from omkjmodules.OmikujiBox import OmikujiBox
    from omkjmodules.OmikujiFactory import OmikujiFactory

    NUMBERS_OF_OMIKUJI = 100

    omikuji_properties = OmikujiProperties()
    omikuji_writer = OmikujiWriter(omikuji_properties)
    omikuji_box = OmikujiBox()

    omkjf = OmikujiFactory(NUMBERS_OF_OMIKUJI, omikuji_writer, omikuji_box)
    omkjb = omkjf.get_omikuji_box()
    for i in range(5):
        omkj = omkjb.get_omikuji()
        print(omkj.get_vars())

    return 0


if __name__ == '__main__':
    import sys
    import os

    sys.path.append(os.path.join(os.path.dirname(__file__), "omkjmodules"))
    sys.exit(main())
