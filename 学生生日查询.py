password = input('输入密码以启动【什亭之匣】：')
if password =='吾等所望那七声的哀叹吾等犹记杰里科的古则':
    print('连接密码验证成功')
    print('欢迎登陆【什亭之匣】，老师')
    yuan = input('输入学院(阿拜多斯，圣三一，歌赫娜，千禧年科技，红东联邦，山海经，瓦尔基里，百鬼夜行，阿里乌斯，SRT)：')
    if yuan =='阿拜多斯':
        birthday1={'砂狼白子':'5月16日','小鸟游星野':'1月2日','十六夜野宫':'9月1日','黑见芹香':'6月25日','奥空绫音':'11月12日'}
        choosea=str(input('输入在阿拜多斯的学生：'))
        if choosea in birthday1:
            print(choosea+'的生日是'+birthday1[choosea])
        else:
            print('该学生不属于阿拜多斯')
    else:
        if yuan=='圣三一':
            birthday2={'圣园未花':'5月8日','白洲梓':'12月26日','栗村爱理':'1月30日','古关忧':'4月23日','桐藤渚':'7月4日','若叶日向':'5月17日',
                       '杏山和纱':'8月5日','百合园圣娅':'9月29日','阿慈谷日富美':'11月27日','静山真白':'6月5日','鹫见芹娜':'1月6日',
                       '浦和花子':'1月3日','剑先鹤城':'6月24日','朝颜花江':'5月12日','伊落玛丽':'9月12日','羽川莲见':'12月12日','仲正一花':'11月11日',
                       '伊原木好美':'8月29日','苍森美祢':'11月23日','河驹风兰舞':'5月6日','柚鸟夏':'12月4日','宇泽玲纱':'5月31日','下江小春':'4月16日',
                       '守月铃美':'8月31日','圆堂志美子':'11月30日','歌住樱子':'10月4日'}
            chooseb=str(input('输入在圣三一的学生：'))
            if chooseb in birthday2:
                print(chooseb+'的生日是：'+birthday2[chooseb])
            else:
                print('该学生不属于圣三一')
        elif yuan=='歌赫娜':
            birthday3={'伊吕波':'11月16日'}
            choosec=str(input('输入在歌赫娜的学生：'))
            if choosec in birthday3:
                print(choosec+'的生日是'+birthday3[choosec])
            else:
                print('该学生不属于歌赫娜')
        elif yuan== '千禧年科技':
            birthday4={'早濑优香':'3月14日',}
            choosed=str(input('输入在千禧年科技的学生：'))
            if choosed in birthday4:
                print(choosed+'的生日是：'+birthday4[choosed])
            else:
                print('该学生不属于千禧年科技')
        elif yuan == '红冬联邦':
            birthday5={'连河切里诺':'10月27日',}
            choosee=str(input('输入在红东联邦的学生：'))
            if choosee in birthday5:
                print(choosee+'的生日是'+birthday5[choosee])
            else:
                print('该学生不属于红东联邦')     
        elif yuan == '山海经':
            birthday6={'龙华妃咲':'2月19日',}
            choosef=str(input('输入在山海经的学生：'))
            if choosef in birthday6:
                print(choosef+'的生日是：'+birthday6[choosef])
            else:
                print('该学生不属于山海经')
        elif yuan == '瓦尔基里':
            birthday7={'尾刃康娜':'9月7日',}
            chooseg=str(input('输入在瓦尔基里的学生：'))
            if chooseg in birthday7:
                print(chooseg+'的生日是：'+birthday7[chooseg])
            else:
                print('该学生不属于瓦尔基里')
        elif yuan == '百鬼夜行':
            birthday8={'久田泉奈':'12月16日',}
            chooseh=str(input('输入在百鬼夜行的学生:'))
            if chooseh in birthday8:
                print(chooseh+'的生日是：'+birthday8[chooseh])
            else:
                print('该学生不属于百鬼夜行')
        elif yuan =='阿里乌斯':
            birthday9={'秤亚津子':'1月20日',}
            choosei=str(input('输入在阿里乌斯的学生:'))
            if choosei in birthday9:
                print(choosei+'的生日是：'+birthday9[choosei])
            else:
                print('该学生不属于阿里乌斯')
        elif yuan == 'SRT':
            birthday10={'月雪宫子':'1月7日',}
            choosej=str(input('输入在SRT的学生:'))
            if choosej in birthday10:
                print(choosej+'的生日是：'+birthday10[choosej])
            else:
                print('该学生不属于SRT')

            

















else:
    print('密码验证失败')
input('摁下任意键退出')
