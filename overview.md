# 类

## game_launcher:
陈耀信

    主要处理游戏的基础设施、类与类间的通信、每个循环调用各类的update函数、I/O、绘图

    __init__() 
    调用各类的构造函数；初始化pygame的基本组件；初始化精灵Group
    
    launch() 游戏主函数：
    1. 事件监测：处理I/O，调用相应的类接口（如在键盘按下W键时调用player类中的前行函数）
    2. 核心内容：调用接口生成enemy、props并加入精灵Group；检测精灵之间的碰撞；更新精灵Group
    3. 更新精灵Group组件
    4. 刷新窗口

    接口需求（暂定）：
    player：玩家构造函数；player的前进后退左右移动函数；发射子弹的函数；update()
    map：地图构造函数；地图绘制方案（结合视野问题）
    bullet：子弹构造函数；update()
    enemy：敌人构造函数；update()
    props：道具构造函数；update()（注：道具生成逻辑在game_launcher里写吧）


## player
葛苏杭

继承pygame.sprite类

1. 二维运动
2. 发射bullet
3. 与props互动
4. 与地图互动
5. 与enemy互动

#### 数据成员：
血量 子弹数 自己的位置坐标（数组） 状态（props相关） 图片及其rect



## map: 赵涵
1. 提供player移动接口
2. （地图生成？）

#### 数据成员：
地图数组 图片及其rect

***

## 后三个类由张宝樑、杨峻负责

## bullet
继承pygame.sprite类

1. 与地图互动
2. 与enemy互动

#### 数据成员：
子弹的位置坐标（数组） 图片及其rect


## enemy（生成逻辑？
继承pygame.sprite类

1. 与player互动
2. 与地图互动

#### 数据成员：
血量 位置（数组） 图片及其rect


## Props道具(血包 大子弹？)
继承pygame.sprite类

#### 数据成员：
道具类型 图片及其rect