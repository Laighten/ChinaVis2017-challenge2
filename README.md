# ChinaVis2017-challenge2
本项目为本人复现ChinaVIS2017挑战赛2的作品，其中部分界面为自己设计，部分界面参考了一等奖获奖作品
### 一、项目介绍
- 仓库地址：[https://github.com/Laighten/ChinaVis2017-challenge2.git](https://github.com/Laighten/ChinaVis2017-challenge2.git)
#### （1）Geographical
![Geographical](https://github.com/Laighten/ChinaVis2017-challenge2/raw/master/img/图片0.png)
#### （2）AgeTime
![AgeTime](https://github.com/Laighten/ChinaVis2017-challenge2/raw/master/img/图片1.png)
#### （3）illegalBar
![illegalBar](https://github.com/Laighten/ChinaVis2017-challenge2/raw/master/img/图片2.png)
#### （4）Signature
![Signature](https://github.com/Laighten/ChinaVis2017-challenge2/raw/master/img/图片3.png)
### 二、后端部署
必备软件：
- mongodb v3.7.3 其他版本也行
- python 3.0以上
#### python库
```
#安装库：pip install Django==2.0.6
版本要求：
  Django 2.0.6 
  django-cors-headers 2.2.0 
  django-rest-framework-mongoengine 3.4.0 
  djangorestframework 3.10.3 
  pymongo 3.6.1 
  mongoengine 0.17.0 
由于mongodb和Django框架的更新换代，不同版本的库可能出现不适配的问题。 为确保程序正常运行请按上述版本进行安装
```
#### 部署流程
```
#启动mongodb数据库
mongod --dbpath 本地路径\mongoDB_data
#启动Django后台
cd \back\myproject\
python manage.py runserver
```

### 三、前端部署
#### 必备软件：
- node
- Vue 版本2.0
#### 部署流程：
```
cd front/myfirst/
#安装依赖
npm install
#本地启动
npm start
```

