class FoodComputer:
    def __init__(self, user_height, user_weight, target_weight, target_time, tdee, day_total = 2000):
        self.user_height = user_height
        self.user_weight = user_weight
        self.target_weight = target_weight
        self.target_time = target_time
        self.tdee = tdee
        self.day_total = day_total



    # 要達到目標體重，每日可吃多少
    def count_cal_day(self):
        cal = ((self.target_weight - self.user_weight) * 7700 / self.target_time + self.tdee)
        return cal
        

    # 計算當日熱量總和  from user database
    def count_day_total(self, day_total):
        self.day_total = day_total


    # 以目前的每日飲食狀況，target time 到達時，預估體重
    def pred_weight(self):
        w = self.user_weight + (self.day_total - self.tdee) * self.target_time / 7700
        return w
    


if __name__ == '__main__':

    # 讓使用者輸入資訊
    user_height = float(input('身高 = 公分？ '))
    user_weight = float(input('體重 = 公斤？ '))
    target_weight = float(input('目標體重 = 公斤？ '))
    target_time = float(input('目標達成天數 = ? '))
    tdee = float(input('TDEE = ? '))

    # 創建 FoodComputer
    user_info = FoodComputer(user_height, user_weight, target_weight, target_time, tdee)

    # 假設今天吃了1500kcal
    user_info.count_day_total(1500)
    print(f'今天吃了{user_info.day_total} kcal，還可以再吃{user_info.count_cal_day() - user_info.day_total :.1f} kcal ')

    print(f'每天吃{user_info.count_cal_day():.2f} kcal ，{user_info.target_time:.0f}後體重可到達{user_info.target_weight}公斤')
    print(f'以目前的飲食狀況，{user_info.target_time:.0f}天後體重為: {user_info.pred_weight():.2f} 公斤')
