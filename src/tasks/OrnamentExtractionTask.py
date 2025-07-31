from src.tasks.TradeBlazePowerTask import TradeBlazePowerTask


class OrnamentExtractionTask(TradeBlazePowerTask):
    def __init__(self, *args, **kwargs):
        super().__init__('饰品提取', '刷选定的饰品提取关卡，需要有差分宇宙存档', *args, **kwargs)
        self.level = ["月下朱殷", "纷争不休", "蠹役饥肠", "永恒笑剧", "伴你入眠", "天剑如雨", "孽果盘生", "百年冻土",
                      "温柔话语", "浴火钢心", "坚城不倒"]

    def run(self):
        time = self.config.get('次数', 1)
        if not self.page_locate("饰品提取"):
            return
        if not self.level_locate():
            return
        for i in range(30):
            if len(self.ocr(0.86, 0.90, 0.92, 0.92, match="开始挑战", log=True)) != 0:
                break
            self.sleep(0.5)
        else:
            self.log_info('Time out')
            return

        if self.config.get('使用支援角色',False):
            self.click(0.55,0.77, down_time=0.3,after_sleep=0.5)
            self.click(0.15,0.21, down_time=0.3,after_sleep=0.5)
        for i in range(30):
            if len(self.ocr(0.86, 0.90, 0.92, 0.92, match="开始挑战", log=True)) == 0:
                break
            self.click(0.87, 0.91, down_time=0.5)
        if self.replenish_check()==-1:
            self.send_key('esc',after_sleep=1)
            self.send_key('esc', after_sleep=0.5)
            return
        self.wait_ocr(0.03, 0.01, 0.08, 0.04, match="差分宇宙", log=True, time_out=30)
        self.send_key('w', down_time=2.5)
        self.click_no_position()
        time-=1
        for i in range(time):
            self.wait_battle_end(timeout=600)
            self.again()
        else:
            self.wait_battle_end(timeout=600)
        self.quit()
        self.info_set(self.name,'任务完成')
