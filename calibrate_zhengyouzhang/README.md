# 张正友标定法 & OpenCV相机标定实现

## 张正友标定法 原理

Paper: [A Flexible New Technique
for Camera Calibration](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=888718&tag=1) & Nutstore/Papers 笔记。

原理解释参考：

[SLAM入门之视觉里程计(6)：相机标定 张正友经典标定法详解
](https://www.cnblogs.com/wangguchangqing/p/8335131.html)

## OpenCV相机标定实现

### Method1: 使用OpenCV sample
[官方源码 | Github](https://github.com/opencv/opencv/blob/master/samples/cpp/tutorial_code/calib3d/camera_calibration/camera_calibration.cpp)

我的实现：[GitHub](https://github.com/xxhaonan/calibrate_zhengyouzhang/tree/main/ch5/camera_calibration)

资料参考： [OpenCV 相机参数标定（Camera Calibration）](https://www.jianshu.com/p/967a35dbb56a) 参考该篇文章中提到的该sample的调用方法

NOTICE：
* 在OpenCV安装目录中 samples/data 中有拍摄好的标定板图片，可以直接用（不推荐，因为它长宽的格数都一样，可使用上面参考博文中的 9*6 的 chessboard）。
* 实验发现，标定板周围要是白色的才行，黑色的提取不出角点来。
* in_VID5.xml 是输入的一些控制参数，可以根据实际情况进行修改。
* VID5.xml 中输入图片所在目录。

### Method2: 自己写主函数，其中调用OpenCV库函数
我的实现：[GitHub]([https://github.com/Mingrui-Yu/slambook2/tree/master/MingruiSLAM/ch5/cameraCalibration](https://github.com/xxhaonan/calibrate_zhengyouzhang/tree/main/ch5)) 不完整，只写到标定，没写标定结果评估

资料参考：
* [张正友相机标定Opencv实现以及标定流程&&标定结果评价&&图像矫正流程解析（附标定程序和棋盘图）](https://blog.csdn.net/dcrmg/article/details/52939318) 主要参考该篇文章最后的完整代码 (其中定义内参矩阵和畸变系数的Mat格式需要修改)
* [Camera calibration using C++ and OpenCV](https://sourishghosh.com/2016/camera-calibration-cpp-opencv/) 参考其中提到FLAG的设置

NOTICE：
* flag的设置对标定结果有较大影响。
* 拍摄的标定板图片，标定板要小一点，否则提取不出角点。
* 定义内参矩阵的数据格式为Mat::eye(3, 3, CV_64F)， 如果定义为参考文章中的那样，标定后内参矩阵出现-nan。
