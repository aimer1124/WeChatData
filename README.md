# WeixinData
Use Python to deal Weixin Data

- Python: `3.6.1`
- Module

  | Name   |      Summary      |  Github |
  |----------|:-------------:|------:|
  |itchat| 微信个人号接口、微信机器人及命令行微信|[https://github.com/littlecodersh/ItChat](https://github.com/littlecodersh/ItChat)|



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
5. 登录成功后，会给手机微信发送消息`你好`

实现原理

1. itchat 会模拟手机版本的微信，获取登录二微码
2. 通过扫描二维码后，手机登录，登录后可使用微信`网页`版本的功能

核心实现代码`itchat/components/login.py`

