class FoodComputer:
    def __init__(
        self, user_height, user_weight, target_weight, target_time, tdee, day_total=2000
    ):
        self.user_height = user_height
        self.user_weight = user_weight
        self.target_weight = target_weight
        self.target_time = target_time
        self.tdee = tdee
        self.day_total = day_total

    # 要達到目標體重，每日可吃多少
    def count_cal_day(self):
        cal = (
            self.target_weight - self.user_weight
        ) * 7700 / self.target_time + self.tdee
        return cal

    # 計算當日熱量總和  from user database
    def count_day_total(self, day_total):
        self.day_total = day_total

    # 以目前的每日飲食狀況，target time 到達時，預估體重
    def pred_weight(self):
        w = self.user_weight + (self.day_total - self.tdee) * self.target_time / 7700
        return w
