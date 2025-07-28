/*
函数功能描述:存储一个关节点位信息
id - 存储点位id号,从1开始,注意该id与CARTPoint的点位id号各自独立
double j1-j6 - 6个关节位置,单位是度
*/
int JNTPoint(int id, double j1, double j2, double j3, double j4, double j5, double j6)
例子:JNTPoint(1,10,11,12,13,14,15)



/*
函数功能描述:存储一个笛卡尔点位信息
id - 存储点位id号,从1开始,注意该id与JNTPoint的点位id号各自独立
double x,y,z,rx,ry,yz - 笛卡尔点位信息,位置单位是mm,角度单位是度
*/
int CARTPoint(int id, double x,y,z,rx,ry,rz)//存储一个笛卡尔空间点位
例子：CARTPoint(1,100,110,200,0,0,0)



/*
函数功能描述:获取指定序号点的关节或者笛卡尔位置信息
string name - 'JNT'或者'CART',JNT代表获取关节点位信息,'CART'代表获取笛卡尔点位信息
int id - 点位id,从1开始
*/
string GET(string name, int id)//获取对应id序号点位的内容,name可以输入JNT或者CART
例子：GET(JNT,1)



/*
函数功能描述:拖动模式开关
uint8_t state - 1-打开拖动模式,0-关闭拖动模式
*/
int DragTeachSwitch(uint8_t state)
例子：DragTeachSwitch(0)



/*
函数功能描述:机械臂使能开关
uint8_t state - 1-机械臂使能,0-机械臂去使能
*/
int RobotEnable(uint8_t state)
例子：RobotEnable(1)



/*
函数功能描述:模式切换
uint8_t state - 1-手动模式,0-自动模式
*/
int Mode(uint8_t state)
例子：Mode(1)



/*
函数功能描述:设置当前模式下机械臂速度
float vel - 速度百分比,范围为1-100
*/
int SetSpeed(float vel)
例子：SetSpeed(10)



/*
函数功能描述:设置并加载指定序号的工具坐标系
int id - 工具坐标系编号,范围1-15
float x,y,z,rx,ry,rz - 工具坐标系的偏移量信息
*/
int SetToolCoord(int id, float x,float y, float z,float rx,float ry,float rz)
例子：SetToolCoord(1,0,0,0,0,0,0)



/*
函数功能描述:设置工具坐标系列表
int id - 工具坐标系编号,范围1-15
float x,y,z,rx,ry,rz - 工具坐标系的偏移量信息
*/
int SetToolList(int id, float x,float y, float z,float rx,float ry,float rz );
例子：SetToolList(1,0,0,0,0,0,0)



/*
函数功能描述:设置外部工具坐标系
int id - 工具坐标系编号,范围1-15
float x,y,z,rx,ry,rz - 外部工具坐标系的偏移量信息
*/
int SetExToolCoord(int id, float x,float y, float z,float rx,float ry,float rz);	
例子：SetExToolCoord(1,0,0,0,0,0,0)



/*
函数功能描述:设置外部工具坐标系列表
int id - 工具坐标系编号,范围1-15
float x,y,z,rx,ry,rz - 外部工具坐标系的偏移量信息
*/
int SetExToolList(int id, float x,float y, float z,float rx,float ry,float rz);
例子：SetExToolList(1,0,0,0,0,0,0)



/*
函数功能描述:设置工件坐标系
int id - 工件坐标系编号,范围1-15
float x,y,z,rx,ry,rz - 工件坐标系的偏移量信息
*/
int SetWObjCoord(int id, float x,float y, float z,float rx,float ry,float rz);
例子：SetWObjCoord(1,0,0,0,0,0,0)



/*
函数功能描述:设置工件坐标系列表
int id - 工件坐标系编号,范围1-15
float x,y,z,rx,ry,rz - 工件坐标系的偏移量信息
*/
int SetWObjList(int id, float x,float y, float z,float rx,float ry,float rz);
例子：SetWObjList(1,0,0,0,0,0,0)



/*
函数功能描述:设置末端负载重量
float weight - 负载重量,单位kg
*/
int SetLoadWeight(float weight);
例子：SetLoadWeight(3.5)



/*
函数功能描述:设置末端负载质心坐标
float x,y,z - 质心坐标,单位为mm
*/
int SetLoadCoord(float x,float y,float z);
例子：SetLoadCoord(10,20,30)



/*
函数功能描述:设置机器人安装方式
uint8_t install - 安装方式,0-正装,1-侧装,2-倒装
*/
int SetRobotInstallPos(uint8_t install);
例子：SetRobotInstallPos(0)



/*
函数功能描述:设置机器人安装角度,自由安装
double yangle - 倾斜角
double zangle - 旋转角
*/
int SetRobotInstallAngle(double yangle,double zangle);
例子：SetRobotInstallAngle(90,0)




//安全配置
/*
函数功能描述:设置机器人碰撞等级
float level1-level6 - 1-6轴的碰撞等级,范围是1-10
*/
int SetAnticollision(float level1, float level2, float level3, float level4, float level5, folat level6);
例子：SetAnticollision(1,1,1,1,1,1)



/*
函数功能描述:设置碰撞后策略
int strategy - 0-报错停止,1-继续运行
*/
int SetCollisionStrategy(int strategy);
例子：SetCollisionStrategy(1)



/*
函数功能描述:设置正限位,注意设置值必须在硬限位范围内
float limit1-limit6 - 6个关节限位值
*/
int SetLimitPositive(float limit1, float limit2, float limit3, float limit4, float limit5, float limit6);
例子：SetLimitPositve(100,90,90,90,90,90)



/*
函数功能描述:设置负限位,注意设置值必须在硬限位范围内
float limit1-limit6 - 6个关节限位值
*/
int SetLimitNegative(float limit1, float limit2, float limit3, float limit4, float limit5, float limit6);
例子：SetLimitNegative(-100,-90,-90,-90,-90,-90)



/*
函数功能描述:错误状态清除
*/
int ResetAllError();



/*
函数功能描述:关节摩擦力补偿开关
uint8_t state - 0-关, 1-开
*/
int FrictionCompensationOnOff(uint8_t state);
例子：FrictionCompensationOnOff(1)



/*
函数功能描述:设置关节摩擦力补偿系数-正装
float coeff1-coeff6 - 6个关节补偿系数,范围是0-1
*/
int SetFrictionValue_level(float coeff1,float coeff1,float coeff3,float coeff4,float coeff5,float coeff6);
例子：SetFrictionValue_level(1,1,1,1,1,1)



/*
函数功能描述:设置关节摩擦力补偿系数-侧装
float coeff1-coeff6 - 6个关节补偿系数,范围是0-1
*/
int SetFrictionValue_wall(float coeff1,float coeff1,float coeff3,float coeff4,float coeff5,float coeff6);
例子：SetFrictionValue_wall(0.5,0.5,0.5,0.5,0.5,0.5)



/*
函数功能描述:设置关节摩擦力补偿系数-倒装
float coeff1-coeff6 - 6个关节补偿系数,范围是0-1
*/
int SetFrictionValue_ceiling(float coeff1,float coeff1,float coeff3,float coeff4,float coeff5,float coeff6);
例子：SetFrictionValue_ceiling(0.5,0.5,0.5,0.5,0.5,0.5)



//外设控制
/*
函数功能描述:激活夹爪
int index - 夹爪编号
uint8_t act - 0-复位, 1-激活
*/
int ActGripper(int index,uint8_t act);
例子：ActGripper(1,1)



/*
函数功能描述:控制夹爪
int index - 夹爪编号
int pos - 位置百分比,范围0-100
*/
int MoveGripper(int index,int pos);
例子：MoveGripper(1,10)



//IO控制
/*
函数功能描述:设置控制箱数字量输出
int id - io编号,范围0-15
uint_t status - 0-关, 1-开
*/
int SetDO(int id,uint8_t status);
例子：SetDO(1,1)



/*
函数功能描述:设置工具数字量输出
int id - io编号,范围0-1
uint_t status - 0-关, 1-开
*/
int SetToolDO(int id,uint8_t status);
例子：SetToolDO(0,1)



/*
函数功能描述:设置控制箱模拟量输出
int id - io编号,范围0-1
float vlaue - 电流或者电压值百分比,范围0-100
*/
int SetAO(int id,float value);
例子：SetAO(1,100)



/*
函数功能描述:设置工具模拟量输出
int id - io编号,范围0
float vlaue - 电流或者电压值百分比,范围0-100
*/
int SetToolAO(int id,float value);
例子：SetToolAO(0,100)



//运动指令
/*
函数功能描述:机器人点动
uint8_t ref - 0-关节点动, 2-基坐标系下点动, 4-工具坐标系下点动, 8-工件坐标系下点动
uint8_t nb - 1-关节1(或x轴),2-关节2(或y轴),3-关节3(或z轴),4-关节4(或绕x轴旋转),5-关节5(或绕y轴旋转),6-关节6(或绕z轴旋转)
uint8_t dir - 0-负方向, 1-正方向
float vel - 速度百分比, 范围为0-100
*/
int StartJOG(uint8_t ref, uin8_t nb, uint8_t dir, float vel);
例子：StartJOG(1,1,1,10)


/*
函数功能描述:机器人点动停止
uint8_t ref - 0-关节点动停止, 2-基坐标系下点动停止, 4-工具坐标系下点动停止, 8-工件坐标系下点动停止
*/
int StopJOG(uint8_t ref);
例子：StopJOG(1)


/*
函数功能描述:机器人点动立即停止
*/
int ImmStopJOG();



/*
函数功能描述:关节空间运动
string point_name - 预存点位名称,比如JNT1就是关节点位信息序号为1的点位,CART1就是笛卡尔点位信息序号为1的点位,MoveJ指令支持输入关节点位或者笛卡尔点位。需要注意的,MoveJ指令由于默认参数中有指定工具坐标系和工件坐标系,当这两个坐标系序号与当前加载的不一致时,该指令会导致报错,需要在默认参数中修改坐标系参数并load参数后再运行该运动指令。
string point_name - 预存点位名称,比如JNT1就是关节点位信息序号为1的点位,CART1就是笛卡尔点位信息序号为1的点位,MoveJ指令支持输入关节点位或者笛卡尔点位。
float vel - 指令速度百分比,范围0-100
int tool_num - 工具坐标系号
int user_num - 工件坐标系号
*/
int MoveJ(string point_name, float vel,int tool_num,int user_num);//point_name是输入预存点位信息,
例子：MoveJ(JNT1,10,0,1)

/*
函数功能描述:笛卡尔空间直线运动
string point_name - 预存点位名称,比如JNT1就是关节点位信息序号为1的点位,CART1就是笛卡尔点位信息序号为1的点位,MoveL指令支持输入关节点位或者笛卡尔点位。需要注意的,MoveL指令由于默认参数中有指定工具坐标系和工件坐标系,当这两个坐标系序号与当前加载的不一致时,该指令会导致报错,需要在默认参数中修改坐标系参数并load参数后再运行该运动指令。
float vel - 指令速度百分比,范围0-100
*/
int MoveL(string point_name,float vel);
例子：MoveL(CART1,10)



/*
函数功能描述:笛卡尔空间圆弧运动
string point1_name point2_name - 预存点位名称,比如JNT1就是关节点位信息序号为1的点位,CART1就是笛卡尔点位信息序号为1的点位,MoveC指令支持输入关节点位或者笛卡尔点位,但是两个点位必须同类型的,即不支持第一个点位输入关节空间点位,第二个点位输入笛卡尔点位。需要注意的,MoveC指令由于默认参数中有指定工具坐标系和工件坐标系,当这两个坐标系序号与当前加载的不一致时,该指令会导致报错,需要在默认参数中修改坐标系参数并load参数后再运行该运动指令。
float vel - 指令速度百分比,范围0-100
*/
int MoveC(string point1_name,string point2_name, float vel);
例子：MoveC(JNT1,JNT2,10)



/*
函数功能描述:样条运动开始
*/
int SplineStart();



/*
函数功能描述:关节空间样条运动,该指令只支持输入JNT1这样的关节数据,输入笛卡尔点位会报错
string point_name - 预存点位名称,比如JNT1就是关节点位信息序号为1的点位。
float vel - 速度百分比,范围0-100
*/
int SplinePTP(string point_name, float vel);
例子：SplinePTP(JNT2,10)



/*
函数功能描述:样条运动结束
*/
int SplineEnd();



/*
函数功能描述:笛卡尔空间样条运动开始
uint8_t ctlpoint - 0-轨迹经过路径点, 1-轨迹不经过控制点,至少4个点
*/
int NewSplineStart(uint8_t ctlpoint);
例子：NewSplineStrart(1)



/*
函数功能描述:笛卡尔空间样条运动,只能输入CART1这样的笛卡尔空间点位,输入关节空间点位会报错
string point_name - 预存点位名称,比如CART1就是笛卡尔空间点位信息序号为1的点位。
float vel - 速度百分比,范围0-100
int lastflag - 0-不是最后一个点, 1-是最后一个点
*/
int NewSplinePoint(string point_name, float vel, int lastflag);
例子：NewSplinePoint(JNT2,20,0)



/*
函数功能描述:笛卡尔空间样条运动结束
*/
int NewSplineEnd();



/*
函数功能描述:停止运动
*/
int StopMotion();



/*
函数功能描述:点位整体偏移开始
int flag - 0-基坐标系下/工件坐标系下偏移, 2-工具坐标系下偏移
double x,y,z,rx,ry,rz - 偏移位姿量
*/
int PointsOffsetEnable(int flag,double x,double y,double z,double rx,double ry,double rz);
例子：PointsOffsetEnable(1,10,10,10,0,0,0)



/*
函数功能描述:点位整体偏移结束
*/
int PointsOffsetDisable();
