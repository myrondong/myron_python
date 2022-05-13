import pytest
import yaml


class YamlUtil:
    def __init__(self,yaml_file):
        """
        初始化yaml 文件path
        :param yaml_file:
        """
        self.yaml_file = yaml_file

    def read_yaml(self):
        """
        读取yaml 文件，反序列化，就是把yaml 格式转换成字典格式
        :return:
        """
        with open(self.yaml_file,'r',encoding='utf-8') as f:
            value = yaml.load(f,Loader=yaml.FullLoader)
            print(value)
            return value