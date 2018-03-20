# WeixinData
Use Python to deal Weixin Data

- Python: `3.6.1`
- Module

  | Name   |      Summary      |  Github |
  |----------|:-------------:|------:|
  |itchat| 微信个人号接口、微信机器人及命令行微信|[https://github.com/littlecodersh/ItChat](https://github.com/littlecodersh/ItChat)|


## 第二步，获取微信好友中，男女比例

- 获取好友列表

```
itchat.get_friends()
```

- 分析微信`好友数据`结构

![好友数据结构](./img/friendData.png)


- 从数据结构可以看出，如果想获取性别，只需要读取`sex`字段的值

```python
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
```

- 查看的所有好友的性别分布

```
男性好友：61.67%
女性好友：32.62%
其他：5.71%
```

## 第一步，调用微信登录，实现微信消息发送

```python
import itchat
itchat.login()# 发送消息
itchat.send(u'你好', 'filehelper')
```

实现流程

1. 生成微信登录二微码图片
2. 保存至本机
3. 自动打开登录二微码图片
4. 手机扫描微信二微码图片，实现网页版微信登录
5. 登录成功后，会删除本机的微信登录二微码
6. 给手机端微信发送消息`你好`

实现原理

1. itchat 会模拟手机版本的微信，获取登录二微码
2. 通过扫描二维码后，手机登录，登录后可使用微信`网页`版本的功能

核心实现代码`itchat/components/login.py`

