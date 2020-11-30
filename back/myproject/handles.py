from Mongodata import JuvCount, JuvRed, JuvBlue, ClickTime18, Juvdetail, geo_data
from Mongodata import ClickTimeOver18, AvgTime, AvgDayTime, AgeTimeNum, ApiAll
import time

if __name__ == '__main__':
    start = time.clock()
    tomomgo_JuvCount = JuvCount()
    tomomgo_JuvCount.Juvdata()

    tomongo_JuvRed = JuvRed()
    tomongo_JuvRed.JuvNo()
    
    tomomgo_JuvBlue = JuvBlue()
    tomomgo_JuvBlue.JuvInf()

    tomongo_ClickTime18 = ClickTime18()
    tomongo_ClickTime18.Time18()

    tomongo_ClickTimeOver18 = ClickTimeOver18()
    tomongo_ClickTimeOver18.TimeOver18()

    tomongo_AvgTime = AvgTime()
    tomongo_AvgTime.Atime()

    tomongo_AvgDayTime = AvgDayTime()
    tomongo_AvgDayTime.ADtime()

    tomongo_AgeTimeNum = AgeTimeNum()
    tomongo_AgeTimeNum.ATN()

    tomongo_Juvdetail = Juvdetail()
    tomongo_Juvdetail.Detail()

    tomongo_ApiAll = ApiAll()
    tomongo_ApiAll.All()

    tomongo_geo_data = geo_data()
    tomongo_geo_data.data_geo()