import pandas as pd

class AgeCsv:
    Immigration = pd.read_csv('..\\..\\processed_csv\\processed_two\\hydata_count.csv', sep=',', low_memory=False, header=0)
    Immigration['AREAID'] = Immigration['AREAID'].astype(int)
    Immigration['AREAID'] = Immigration['AREAID'] / 100
    Immigration['AREAID'] = Immigration['AREAID'].astype(int)
    local = Immigration[Immigration['AREAID'] == 5102]
    Immigration = Immigration[Immigration['AREAID'] != 5102]
    GuangYuan = Immigration[Immigration['AREAID'] == 5108]
    MianYang = Immigration[Immigration['AREAID'] == 5107]
    NanChong = Immigration[Immigration['AREAID'] == 5113]
    ChengDu = Immigration[Immigration['AREAID'] == 5101]
    ShuiNing = Immigration[Immigration['AREAID'] == 5109]
    GuangAn = Immigration[Immigration['AREAID'] == 5116]
    NeiJiang = Immigration[Immigration['AREAID'] == 5110]
    ZiGong = Immigration[Immigration['AREAID'] == 5103]
    NuZhou = Immigration[Immigration['AREAID'] == 5105]
    YiBing = Immigration[Immigration['AREAID'] == 5115]
    TongRen = Immigration[Immigration['AREAID'] == 5227]
    BiJie = Immigration[Immigration['AREAID'] == 5226]
    Area = {'GuangYuan': len(GuangYuan),'MianYang': len(MianYang),'NanChong':len(NanChong),'ChengDu':len(ChengDu)
            ,'ShuiNing' :len(ShuiNing),'GuangAn':len(GuangAn),'NeiJiang':len(NeiJiang),'ZiGong':len(ZiGong),
            'NuZhou':len(NuZhou),'YiBing':len(YiBing),'TongRen':len(TongRen),'BiJie':len(BiJie)}
    Area = pd.DataFrame(Area, index=[0])
    Area.to_csv('..\\..\\processed_csv\\processed_two\\AreaImmigra.csv', index=0, sep=',')
    Immigration['AREAID'] = Immigration['AREAID'] / 100
    Immigration['AREAID'] = Immigration['AREAID'].astype(int)
    SiChuan = Immigration[Immigration['AREAID'] == 51]
    SiChuan_Male = SiChuan[SiChuan['XB'] == '男']
    SiChuan_Female = SiChuan[SiChuan['XB'] == '女']

    GuiZhou = Immigration[Immigration['AREAID'] == 52]
    GuiZhou_Male = GuiZhou[GuiZhou['XB'] == '男']
    GuiZhou_Female = GuiZhou[GuiZhou['XB'] == '女']

    HuBei = Immigration[Immigration['AREAID'] == 42]
    HuBei_Male = HuBei[HuBei['XB'] == '男']
    HuBei_Female = HuBei[HuBei['XB'] == '女']

    HuNan = Immigration[Immigration['AREAID'] == 43]
    HuNan_Male = HuNan[HuNan['XB'] == '男']
    HuNan_Female = HuNan[HuNan['XB'] == '女']

    HeNan = Immigration[Immigration['AREAID'] == 41]
    HeNan_Male = HeNan[HeNan['XB'] == '男']
    HeNan_Female = HeNan[HeNan['XB'] == '女']

    JangXi = Immigration[Immigration['AREAID'] == 36]
    JangXi_Male = JangXi[JangXi['XB'] == '男']
    JangXi_Female = JangXi[JangXi['XB'] == '女']

    YunNan = Immigration[Immigration['AREAID'] == 53]
    YunNan_Male = YunNan[YunNan['XB'] == '男']
    YunNan_Female = YunNan[YunNan['XB'] == '女']

    AnHui = Immigration[Immigration['AREAID'] == 34]
    AnHui_Male = AnHui[AnHui['XB'] == '男']
    AnHui_Female = AnHui[AnHui['XB'] == '女']

    Shanxi = Immigration[Immigration['AREAID'] == 61]
    Shanxi_Male = Shanxi[Shanxi['XB'] == '男']
    Shanxi_Female = Shanxi[Shanxi['XB'] == '女']

    JangShu = Immigration[Immigration['AREAID'] == 32]
    JangShu_Male = JangShu[JangShu['XB'] == '男']
    JangShu_Female = JangShu[JangShu['XB'] == '女']

    GanSu = Immigration[Immigration['AREAID'] == 62]
    GanSu_Male = GanSu[GanSu['XB'] == '男']
    GanSu_Female = GanSu[GanSu['XB'] == '女']

    Male = {
        'SiChuan':len(SiChuan_Male),'GuiZhou':len(GuiZhou_Male),'HuBei':len(HuBei_Male),
        'HuNan':len(HuNan_Male),'HeNan':len(HeNan_Male),'JangXi': len(JangXi_Male),'YunNan':len(YunNan_Male),
        'AnHui':len(AnHui_Male),'Shanxi':len(Shanxi_Male),'JangShu':len(JangShu_Male),
        'GanSu':len(GanSu_Male)
    }
    Female = {
        'SiChuan': len(SiChuan_Female), 'GuiZhou':len(GuiZhou_Female), 'HuBei':len(HuBei_Female),
        'HuNan':len(HuNan_Female),'HeNan': len(HeNan_Female), 'JangXi': len(JangXi_Female), 'YunNan': len(YunNan_Female),
        'AnHui': len(AnHui_Female), 'Shanxi': len(Shanxi_Female), 'JangShu': len(JangShu_Female),
        'GanSu': len(GanSu_Female)
    }
    AreaProvince1 = pd.DataFrame(Male, index=[0])
    AreaProvince2 = pd.DataFrame(Female, index=[0])
    AreaProvince1 = AreaProvince1.append(AreaProvince2, ignore_index=True)
    AreaProvince1.to_csv('..\\..\\processed_csv\\processed_two\\AreaProvince.csv', index=0, sep=',')




