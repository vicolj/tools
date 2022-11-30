import winsound
import time


'''
    @breaf 这是属于程序员自己的番茄工作法。

    win自带啊。为什么要自己写呢？

    因为win自带的专注太难用，一直到时间的不提醒我！！！！！！！！！！！！！！！！！！
    经常没有任何通知


'''

all_number = 4 # 2h
focus_time = 60 * 25
relax_time = 60 * 5
index = 0


def start():
    global all_number
    global focus_time
    global relax_time
    global index

    while all_number:
        all_number -= 1
        # 专注
        print("start focus " + str(focus_time / 60) + " min")
        winsound.PlaySound("top_gun_classified.wav", winsound.SND_FILENAME)
        
        print("start relax tiem " + str(relax_time / 60))
        time.sleep(focus_time)
        index += 1
        print("over " + str(index) + " min times")
        winsound.PlaySound("relax.wav", winsound.SND_FILENAME)
        if index != 1:
            time.sleep(relax_time)

if __name__ == '__main__':
    start()

