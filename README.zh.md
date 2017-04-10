# Distance(远方) - 世界上遥远的距离

![][badge-author] ![][badge-build] ![][badge-version] ![][badge-python] ![][badge-license]

[English version][readme-en]

Distance(远方)主要使用 Python 语言编写，使用 Flask 作为 Web 框架，用于找到指定位置及其对跖点的地理位置。

数据使用了高德地图(国内)和谷歌地图的 API。


## 简介

Distance(远方) 是一个找到某地以及对应的对跖(zhí)点(antipodes)的系统，即找到该位置在地球上距离最远的地方。它包括:

- [**/**][home]： 找到当前位置(国内，包括港澳台)与对跖点的地理位置。
  - 输入: 北京天安门
- [**/googlemap**][googlemap]： 找到当前位置(全球)与对跖点的地理位置。
  - 输入: New York City
- [**/latlng**][latlng]： 找到给定经纬度的地理位置。
  - 输入格式: 39, 112 (纬度, 经度)


计划实现的其他功能：

- 一个 RESTful API 后端
- 发送查询结果到邮箱

> **对跖点**（英语：antipodes），亦有人称为对跖地，为地理学与几何学上的名词。球面上任一点与球心的连线会交球面于另一点，亦即位于球体直径两端的点，这两点互称为对跖点。也就是说，从地球上的某一地点向地心出发，穿过地心后所抵达的另一端，就是该地点的对跖点。因此，对跖点也可称为地球的相对极。**某位置的对跖点是该位置在地球上距离最远的地方。**

## Demo

这里有一个使用 Distance 建立的[网站][home]。

主页大概长这样:

![](http://ww1.sinaimg.cn/large/647dc635ly1fegrbro6hgj20zz0hzmxp.jpg)


输入你想要查询的地理位置(国内),下图是示例:

![/](http://ww1.sinaimg.cn/large/647dc635ly1fegrf68boog21hb0q01kz.gif)


如果你想要查询国外的地址，请使用 [/googlemap][googlemap]。后端使用的 Google Maps API 访问较慢，如果不是查询国外的地址，请使用国内版本。下图是示例:

![/googlemap](http://ww1.sinaimg.cn/large/647dc635ly1fegrmeii8yg21hb0q3hdt.gif)


如果你想查询经纬度对应的地理位置，请使用[/latlng][latlng]。下面是示例:

![/latlng](http://ww1.sinaimg.cn/large/647dc635ly1fegrrtiu4jg21h80pz7wi.gif)

### 其他玩法

如果你想看看远方到底是什么样子，可以使用 Google 提供的街景地图，仅限国外哦。原因你懂的。

![](http://ww1.sinaimg.cn/large/647dc635ly1fegs4mq2dgg20i90jpb2g.gif)


动图录制的有点糊，实际效果还是很清晰的，大家可以自己试着去探索一下。

## 部署

想在自己的服务器上部署该系统, 请看 Distance [部署文档][deploy-doc]。

## 协助开发

- Fork
- 从 dev 分支新建一个分支
- 写代码，注释和文档，并使用有意义的 commit message 提交
- 将自己加入 CONTRIBUTIONS.md，并且描述你做了什么
- PR 到 dev 分支

在 [CONTRIBUTIONS.md][contributors] 里可以看到贡献者名单。


## 致谢

- 感谢谷歌地图 API 的开发团队
- 感谢高德地图 API 的开发团队
- 感谢 Python 编程语言以及她的开发团队
- 感谢 Flask 的开发团队
- 感谢 Flask-GoogleMaps 的开发团队
- 感谢 Atom 编辑器和她的开发团队
- 感谢开源精神

## License

Distance 系统的所有代码均基于 GPL 协议开源。

详见 [LICENSE][license] 文件。

[readme-en]: https://github.com/RayYu03/Distance/blob/master/README.md

[badge-author]:https://img.shields.io/badge/Author-RayYu03-blue.svg
[badge-build]:https://img.shields.io/badge/build-passing-brightgreen.svg
[badge-version]: https://img.shields.io/badge/version-0.1.0-blue.svg
[badge-license]: https://img.shields.io/badge/license-GPL-blue.svg
[badge-python]: https://img.shields.io/badge/pythin-3.5%2C%203.6-blue.svg

[badge-python]: https://img.shields.io/badge/pythin-3.5%2C%203.6-blue.svg


[home]: http://thefurthestdistance.xyz/
[googlemap]: http://thefurthestdistance.xyz/googlemap
[latlng]: http://thefurthestdistance.xyz/latlng


[contributors]: https://github.com/RayYu03/Distance/blob/master/CONTRIBUTORS.md

[deploy-doc]: https://github.com/RayYu03/Distance/blob/master/deploy.zh.md

[license]: https://github.com/RayYu03/Distance/blob/master/LICENSE
