import re

from src.tasks.TradeBlazePowerTask import TradeBlazePowerTask


class EchoOfWarTask(TradeBlazePowerTask):
    def __init__(self, *args, **kwargs):
        super().__init__("历战余响", "行迹高级材料/光锥", *args, **kwargs)
        self.level=[re.compile('晨昏'),re.compile('心兽'),re.compile('尘梦'),re.compile('蛀星'),
                    re.compile('不死'),re.compile('寒潮'),re.compile('毁灭')]

    def run(self):
        if not self.page_locate("历战余响", True):
            return
        if not self.level_locate(y_offset=90):
            return
        self.set_battle_number()
        self.battle()
        self.info_set(self.name,'任务完成')