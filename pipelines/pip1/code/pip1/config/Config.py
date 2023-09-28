from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, twsr: str=None, fefefg: bool=None, **kwargs):
        self.spark = None
        self.update(twsr, fefefg)

    def update(self, twsr: str="ewfwef", fefefg: bool=True, **kwargs):
        prophecy_spark = self.spark
        self.twsr = twsr
        self.fefefg = self.get_bool_value(fefefg)
        pass
