# Distance - Find the furthest distance in the world.

![][badge-author] ![][badge-build] ![][badge-version] ![][badge-python] ![][badge-license]

[中文版][readme-zh]

Distance is a web application that using Flask as Web framework. In order to find the furthest distance in the world from your location.

Data using Gaode Maps API(in China) and Google Maps API.

## Introduction

Distance is a system that find specific location and antipodes. In other words, it's a system that find the furthest distance in the world from your location.includes:

- [**/**][home]: Find the geographical position of the current location and antipodes. (The current position must be in China)
  - Input: 北京天安门  (Simplified Chinese)
- [**/googlemap**][googlemap]: Find the geographical position of the current location and antipodes.
  - Input: New York City  (Simplified Chinese or English)
- [**/latlng**][latlng]: Find the location of a given latitude and longitude.
  - Input: 39, 112  (lat,lng)

### Other parts (in plan)

- A RESTful API server
- Send the query result to the mail

> **Antipode**: The antipode of any place on the Earth is the place that is diametrically opposite it, so a line drawn from the one to the other passes through the centre of the Earth and forms a true diameter. For example, the antipodes of New Zealand's lower North Island lie in Spain. Most of the Earth's land surfaces have ocean at their antipodes, this being a consequence of most land being in the land hemisphere.

## Demo


There is a [Web][home] site built with Distance, just try it.

homepage:

![](http://ww1.sinaimg.cn/large/647dc635ly1fegrbro6hgj20zz0hzmxp.jpg)


Input a location(in China). For example:

![/](http://ww1.sinaimg.cn/large/647dc635ly1fegrf68boog21hb0q01kz.gif)

If you want to query the foreign address, using [/googlemap][googlemap]. For example:

![/googlemap](http://ww1.sinaimg.cn/large/647dc635ly1fegrmeii8yg21hb0q3hdt.gif)


If you want to query the longitude and latitude corresponding geographic location, using [/latlng][latlng]. For example:

![/latlng](http://ww1.sinaimg.cn/large/647dc635ly1fegrrtiu4jg21h80pz7wi.gif)

### Other functions

If you want to see the appearance of the distance, just using Google street view. For example:

![](http://ww1.sinaimg.cn/large/647dc635ly1fegs4mq2dgg20i90jpb2g.gif)

The quality of the picture is a bit poor, but actual effect is very clear. so, just try it.

## Deploy

Want deploy Distance system of you own? Check [Distance Deploy Doc][deploy-doc] for deploy guide.

## Contribution

- Fork me
- Create a new branch from dev branch
- Add your code, comment, document and meaningful commit message
- Add yourself to CONTRIBUTION.md and describe your work
- PR to dev branch

Thanks all contributors!

You can see a list of contributors in [CONTRIBUTIONS.md][contributors].

## Acknowledgements

- Thanks Google Maps and her developers
- Thanks Gaode Maps and her developers
- Thanks Python language
- Thanks Flask Web framework and her developers
- Thanks Flask-GoogleMaps and her developers
- Thanks Atom and her developers
- Thanks open source

## License

All code of Distance system are open source, based on GPL license.

See [LICENSE][license].

[readme-zh]: https://github.com/RayYu03/Distance/blob/master/README.zh.md

[badge-author]:https://img.shields.io/badge/Author-RayYu03-blue.svg
[badge-build]:https://img.shields.io/badge/build-passing-brightgreen.svg
[badge-version]: https://img.shields.io/badge/version-0.1.0-blue.svg
[badge-license]: https://img.shields.io/badge/license-GPL-blue.svg
[badge-python]: https://img.shields.io/badge/pythin-3.5%2C%203.6-blue.svg

[home]: http://thefurthestdistance.xyz/
[googlemap]: http://thefurthestdistance.xyz/googlemap
[latlng]: http://thefurthestdistance.xyz/latlng

[contributors]: https://github.com/RayYu03/Distance/blob/master/CONTRIBUTORS.md

[deploy-doc]: https://github.com/RayYu03/Distance/blob/master/deploy.md

[license]: https://github.com/RayYu03/Distance/blob/master/LICENSE
