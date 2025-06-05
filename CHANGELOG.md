# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [3.2.2](https://gitlab.smartbase.sk/dev/django_smartshop/compare/v3.2.1...v3.2.2) (2020-07)


### Features

* **catalog:** [#11680](http://redmine.smartbase.sk/issues/11680) added custom catalog tiles for categories ([a31d663](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a31d6633a29fa13947a5e9f09f13b307fdb1eda9))
* **exponea:** move product and category exponea event to datalayer ([4c052af](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4c052afb155d1e5cc9aad58eb1d600b75883fd67))
* **generic-slider:** [#11672](http://redmine.smartbase.sk/issues/11672) added generic slider plugin with fields to customize slider settings and style ([d1139cc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d1139cca6127714009acee0fe9fbc7573725b178))
* **healthcheck:** run healthcheck in celery ([b1ed885](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b1ed885c3caf82b41400a7514663cf674fc76867))
* **multi_alias:** redirects with optional aliases ([6f59389](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6f59389f6e8c5fd98b5e1da12ebeee539a23ff72))
* **shopstore:** enable/disable filter for delivery store - checkbox ([bdff95d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bdff95d9b55d561f261ae60633889ee23afe59ad))
* [#11669](http://redmine.smartbase.sk/issues/11669) added invoice about withdraw from cash_register ([9a079ce](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9a079ce89d3c7ef69e11aeb881a3aee0b74b26c1))
* enable/disable instant page in preferences ([947ecc3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/947ecc3c8a7180f0e611d65304d5fa1d8213b633))
* **purchase:** [#11601](http://redmine.smartbase.sk/issues/11601) move purchase number pattern to dynamic preferences and change it from simple numeric sequence into complex pattern sequence ([7863495](https://gitlab.smartbase.sk/dev/django_smartshop/commit/78634957330d2aa15973f9726405d7581a9416cf))
* removed API index ([0a1031c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0a1031c8e66696244ca36a443277648f28222b09))
* rework to withdrawal - not claim, small updates ([ac726c5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ac726c5e3d31ac9549877c086ad45738dd355061))
* RON to EUR conversion for paypal and 24pay ([7decdf9](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7decdf94524f0e3acb70250ca39b2b2f44b949a6))


### Bug Fixes

* add old_price into heureka values ([1c7e9c0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1c7e9c0ab584fbb5e82cf77ac86d8d67f2dea9c9))
* added country to search from filter in stores ([5423a41](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5423a41ccf43c2e5f4cbd23fc99e2bb20ce12f7b))
* fix purchase save method ([4f7050f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4f7050f318a1c266164616c1b7856e917c71f0f5))
* google merchant categories split fix ([5f0c542](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5f0c54219833fa4e5e6361aa987edeff5ab53b7c))
* heureka categorytext ([2020b31](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2020b31b958de302bfd654882ccdac5952c2d3d5))
* removed old package from requirements ([f1e0ef6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f1e0ef6e7813f46176d0d21da09848794f57e117))
* **catalog:** product category url trans ([b34b392](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b34b3923f0a9effcb17feb2790672e8d3517c129))
* **catalog:** URL parmas check or 404 ([99c6da1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/99c6da14f0abe6054fa76fb61153d4f08bfe783c))
* **sitemap:** correct sitemap paths for other than FileSystemStorage ([1d3e39d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1d3e39de3c66852d345bc6d576fc6257850ce35e))



## [3.2.1](https://gitlab.smartbase.sk/dev/django_smartshop/compare/v3.2.0...v3.2.1) (2020-06)


### Features

* reclaim form ([2f5bf8d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2f5bf8d596538c0f83c13fefda1d07f8770af67d))
* **dynamicpages:** [#9943](http://redmine.smartbase.sk/issues/9943) category landing page generator ([0e191c9](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0e191c9bea45ecf6a83c104785d7849bf42ff58a))
* added select quantity picker for mobile devices ([6ff617a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6ff617a4f52850a4adc0feb5f44947c0dbe92b48))
* force admin language ([2c8fae6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2c8fae65dd2014dfc3718e8f6e02733931047d4b))
* RTB House implementation ([c38409a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c38409ae8b4d3210d95c3028f6f55320f5cffede))
* **cms:** remove cms toolbar middleware when user is not in Admins group ([9de2a06](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9de2a06a328919224c22b07fa7a28bfc1f06434f))
* **exchangerate:** [#11106](http://redmine.smartbase.sk/issues/11106) exchange rate functionality ([d53c1bd](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d53c1bde1a4b1918d9f6f04a830fedcebd498a92))
* **heureka:** rework not to use elastic index anymore ([9f1c43d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9f1c43d7f45ea1d87f754cec7c785eb33edb46a1))
* **search:** [#11087](http://redmine.smartbase.sk/issues/11087) add show exact price preference into search content ([ffa062e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ffa062e1205e434ade78c084077e0789b7e3d180))
* remove api index from feed_products ([c44079b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c44079bf8393f1e42782d241c33717ea15a97a89))


### Bug Fixes

* add webp attendance into cms page cache key ([0594ff4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0594ff4cb28a0ddbff5bb96f66198727eb7175ca))
* add webserver to allowed hosts due to pdf creation ([8fae87c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8fae87c8fa795786b24f5ba88a2998865edd1b0e))
* dont call initial fetch on base basket window call ([b5254b8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b5254b81316fb25b1dfda510fdc5b84c4beb6059))
* fix affiliate cookie ([66809fb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/66809fbd24718a211127dba6e641feb64f15d5cf))
* fix autocomplete in offers, add alias into offer email and checker ([e486536](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e48653650b29e1f546f9934ffc5c7367091fd3d3))
* fix build attribute option translations ([c6f109d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c6f109d247519ec8eeb6ef96f76708e81c3cc16f))
* fix catalog order override sort to descending ([2579ec2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2579ec2a6de531832e4228f96529df5eefed7aa3))
* fix condition for price from in search content ([65d06b6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/65d06b6573c96b927bcc72b43e6343a8fc821774))
* fix django cms toolbar custom middleware ([6dd617a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6dd617ad08f3a3efe74833ae423bc77ffd775bae))
* fix exchange rate app name ([7799870](https://gitlab.smartbase.sk/dev/django_smartshop/commit/779987052b4da0a2085e9245d292b0c784d3cedc))
* fix exchange rate app name ([f061117](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f061117e891c43fee75d589f78d9840e20c94549))
* fix host url for essox ([f613daf](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f613daf0617024af7baf87c8614d54b726e1bc33))
* fix missing variable ([a5d7625](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a5d76251ee95819caa70cd512ab22ee0291d74bb))
* fix PSC validation on purchase process ([47ab8d6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/47ab8d68a1a23ee3b4b9419c9010b9fc5d6368dd))
* fix sitemap path from double nested alias folder to single alias folder ([4094f66](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4094f66d5073fec909e6195d010e7934b59c6d93))
* fixed missing group_by_value ([a8a9685](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a8a968561a8cbafe28ffe3401d6abf46ede80f23))
* reload discounts if new product is added to offer variant ([3e24e5a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3e24e5ae102b571ae8fe57ce0d85f7bde65cd071))
* remove column from order history due to column has no header ([4dee43b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4dee43bc790f21ca67bebcb30b9661825a552dd0))
* remove unnecessary import ([be305a5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/be305a5cdb6a83b77a7797ebd25bc0dc08b85914))
* update sold count ([6d2cef7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6d2cef7d03f5e5b552be93dac552f68ab9f2c5a7))
* **admin:** respect permissions in admin menu, remove unpermitted views from menu ([ed690ab](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ed690ab3616622e3328593c5efee19152c05efd7))



## [3.2.0](https://gitlab.smartbase.sk/dev/django_smartshop/compare/v0.2.20...v3.2.0) (2020-05)


### Features

* [#11172](http://redmine.smartbase.sk/issues/11172) grouping by attributeoptiongroupset in catalog ([62a15a8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/62a15a86c66e7270b39f7144f7e5e829f69e1294))
* [#11172](http://redmine.smartbase.sk/issues/11172) range widget for option groups ([31cee25](https://gitlab.smartbase.sk/dev/django_smartshop/commit/31cee2562b6c2acd759fc0e70d8c7d3888c023d9))
* [#11172](http://redmine.smartbase.sk/issues/11172) test fix ([db9965f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/db9965f43954576b2bd4ed536cecfb64f46ae970))
* added Gzip middleware and minifier for HTML ([e3b1c25](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e3b1c250b36968903aaf7979eb425d6bbe0ffe8f))
* detail variants improvements ([4790023](https://gitlab.smartbase.sk/dev/django_smartshop/commit/479002330abb19c7405f7e422e4edabbf60e10fc))
* rework basket seriallizers to use DB ([ddf8260](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ddf8260b5dfff5b618e543c964bee6e1c856aec6))
* **account:** add is_person data show for registration ([18e9a12](https://gitlab.smartbase.sk/dev/django_smartshop/commit/18e9a12a38256c993a2f7e91a71c75ad727e7c16))
* **catalog:** [#10983](http://redmine.smartbase.sk/issues/10983) add preference to show extra store info ([6e0e13f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6e0e13ffaa4244873430b9a1f82760ea599af76b))
* **catalog:** [#11180](http://redmine.smartbase.sk/issues/11180) return end of sale instead of HTTP 404 when user has not allowed for the product ([4df691d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4df691d308b166e9badbbb9bb593dc154f508039))
* **catalog:** product action banners ([4f6ee90](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4f6ee909757f6ad48084723c1a8aaa5df03aa099))
* **comparator:** [#8630](http://redmine.smartbase.sk/issues/8630) create base implementation of products comparator ([21e4d04](https://gitlab.smartbase.sk/dev/django_smartshop/commit/21e4d04928b7c069e6de27d28d828d1e38e421f1))
* **config:** [#9758](http://redmine.smartbase.sk/issues/9758) return constance config as a fallback ([4c6702d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4c6702dc2539537b0bf1c8cc6058a084acfef220))
* **consent:** add alias to given consent ([c90c144](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c90c144f73368b7c191fff88261783707ed1bd82))
* **crm:** [#11314](http://redmine.smartbase.sk/issues/11314) seller which have permission can change shop store without relogging ([4a2e0e2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4a2e0e22183d0b1edeb3d6f3a1dcc2e82bda12f2))
* **customer:** [#10152](http://redmine.smartbase.sk/issues/10152) add locale to birthday months ([a69a67d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a69a67d313562c089f700cf0d254ed9f9c3bd763))
* **deliverydefinition:** [#10340](http://redmine.smartbase.sk/issues/10340) add alias into delivery length definition ([49463f9](https://gitlab.smartbase.sk/dev/django_smartshop/commit/49463f96a33aafbd868efa6c95696f81f43fc7f6))
* **essox:** move from global preferences to alias preferences ([c90db70](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c90db70bb02e10015ef5a3b08b48c2c8b6990f94))
* **exponea:** [#10738](http://redmine.smartbase.sk/issues/10738) add view_category event ([22c11d9](https://gitlab.smartbase.sk/dev/django_smartshop/commit/22c11d9dacec42f53f8f3bedfdeddef7ec4bc814))
* **frontend:** [#10227](http://redmine.smartbase.sk/issues/10227) server-side rendering and optimization of homepage, catalog and product detail ([098be7e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/098be7e15779c974627e8abe661ee24318b7fe57))
* **gopay:** [#11247](http://redmine.smartbase.sk/issues/11247) track all gopay transactions ([f36be14](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f36be1424f5b8da68cbcf1606c616f9866598e6b))
* **heureka:** [#11253](http://redmine.smartbase.sk/issues/11253) mode heureka configs to one place ([9eaadb5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9eaadb5d06724cd2ef16abb4ab24e3e1219db883))
* **heureka:** [#11253](http://redmine.smartbase.sk/issues/11253) move heureka config to one place ([9529ab4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9529ab43fd9f20f79cc3babf22240c1dda8a37c5))
* **mailer:** [#11267](http://redmine.smartbase.sk/issues/11267) add configuration info to order summary email template ([cbeef91](https://gitlab.smartbase.sk/dev/django_smartshop/commit/cbeef910b92ca6e09c4b64af59fad646fcdde77a))
* **product-detail:** on mobile display product description as accordion ([b549233](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b549233c86b7eb4cf70261e597d36bf56189a473))
* **product-detail:** show full product description tabs content without JS ([062511d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/062511dbff9a2dd451bb0f9f39bdc338a4223532))
* [#11216](http://redmine.smartbase.sk/issues/11216) added option to fill mega menu with custom links ([cd41d6a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/cd41d6a79a2b8ea37a61575e8828c5a6fe476c6b))
* 360 images iframe, split stock loading ([ba66ce6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ba66ce6b6c7100ff55b9d8f2066726af3f9dedc0))
* contact departments, small fixes ([4d17640](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4d1764047d11dd03c8347ee585687c979ae89fd3))
* state group option - as special bar with products, different variation for detail (enable in preference) ([ca3ba88](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ca3ba88143ca3b42c191defdcf0b6e537abe1097))
* **purchaseprocess:** [#11207](http://redmine.smartbase.sk/issues/11207) allow seller to select estimated delivery date from today ([341c2f4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/341c2f48072c4255bceaecbfd607d22794579cc9))
* **purchaseprocess:** [#11207](http://redmine.smartbase.sk/issues/11207) allow seller to select estimated delivery date from today ([eb9834b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/eb9834b9562d112d0c02ea74c65bffadf9b60b76))
* **seo:** create blog sitemap based on alias ([6a5cf34](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6a5cf346f926f5ae0e9c45ca989e93a57ebaa696))
* alias variables name ([1c232d1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1c232d1ec3ecfabc86a031bb8353c7ff362a7ada))
* payment error handling ([7fdf30b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7fdf30b10f00d35cf80d570af228bff6720541f4))
* rework Alias Country - add to class to mapping model ([a7ac851](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a7ac85173a3c2f3d642041368815e91f68efd6ce))
* **migrations:** custom smartbase migrations ([0c68a01](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0c68a01a3cc2a35bcb640461df4ebd9a422292a4))
* **pricing:** [#10434](http://redmine.smartbase.sk/issues/10434) fix some uses of default currency ([e8c28b1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e8c28b1d678ac616fe6af431f5f220fa412ac03e))
* **sitemap:** [#9505](http://redmine.smartbase.sk/issues/9505) sitemap for aliases + images ([0598d69](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0598d69af709d0a639cc3f6667798af1c03367cf))
* **templates:** write cached template loader to cache templates according to alias id ([2f4191a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2f4191aa809c45f6b523b85072cdba145d4054f1))
* [#6587](http://redmine.smartbase.sk/issues/6587) robot framework tests gitlab CI integration with catalog pagination tests ([db5fd5b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/db5fd5b59e8fc5f855ab844071ca894284599766))
* [#9336](http://redmine.smartbase.sk/issues/9336) price discount badges + sort in catalog ([c24ec4b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c24ec4ba5291e9decdc86c355922f22356ac062b))
* [#9505](http://redmine.smartbase.sk/issues/9505) WIP sitemaps ([70a4c44](https://gitlab.smartbase.sk/dev/django_smartshop/commit/70a4c4414dd7fc3a0e644e46778dc96617ef19b2))
* [#9762](http://redmine.smartbase.sk/issues/9762) generate dummy fix, tags, blog posts ([6d3cd7b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6d3cd7b16c8afd42a64a7f531c3cc6b14160b1e3))
* [#9762](http://redmine.smartbase.sk/issues/9762) translatable blog and tags ([f32c245](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f32c24561026e89647f9055ac958a8e3ef708499))
* [#9762](http://redmine.smartbase.sk/issues/9762) update package commits ([8c9a097](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8c9a097f35f65646b478afdc83fc79839e23ced8))
* [#9770](http://redmine.smartbase.sk/issues/9770) add alias to context ([2c64ce0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2c64ce0efc0646706f4d8ab0407b123c4f3e53f4))
* [#9771](http://redmine.smartbase.sk/issues/9771) autocomplete for postal code and town according to selected country, parser postal code RO HU ([8427128](https://gitlab.smartbase.sk/dev/django_smartshop/commit/842712846dcb0dbfcb06b547d2e3f96d83f41fcf))
* [#9776](http://redmine.smartbase.sk/issues/9776) hreflang inplementation ([510c737](https://gitlab.smartbase.sk/dev/django_smartshop/commit/510c7375e5516674a0b94d30b549d87c4bc37d05))
* add report builder app ([d80284b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d80284b728fdf65ce33359c6278c8b7fa9c05eb8))
* carousel images, yt attachments, attachments per alias ([f104ad6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f104ad614cab5a80a3ca5a2055e370f30146b269))
* category deepest node call returns default category if there is any, product absolute_url works same ([a73d654](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a73d654dd3ab90d71baa9d350bf5a602e56990ef))
* customizable error 500 page for cloudflare ([f68ab0a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f68ab0a550a854b321f8dbba9859097f7833e0cb))
* enable page cache ([a08cb45](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a08cb450782c559b3d69ae83f50bb1265b097a5a))
* migrations update, materialized view migration, category m2m migration ([91524e5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/91524e5d6d9ef98069846858a109b3feee491abd))
* product categories - M2M through model add ([b510e64](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b510e649c8cc84f92af7eed78ffb76879a7feb8e))
* **alias:** [#9777](http://redmine.smartbase.sk/issues/9777) add alias to country, basket, delivery service, add country to shop store ([b8e2b44](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b8e2b44438d08c8540997e3e13cd5a957373b261))
* **middleware:** create request middleware and move alias assigning from currency middleware to it ([a3ca2bc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a3ca2bce3dcb046d12b6af64a52e92f6e1b15329))
* **preferences:** [#9815](http://redmine.smartbase.sk/issues/9815) alias preferences implementation ([bce883b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bce883b510f20496407d666570ee93e93c88f661))
* **preferences:** [#9875](http://redmine.smartbase.sk/issues/9875) alias preferences constance config fallback implementation ([e566ce3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e566ce301873f8e0dcc3e0c5fa257a2402b7c5cc))
* **preferences:** remove constance config and rewrite global_preferences using get_preference and add email configs for aliases ([075516d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/075516d868129bb7b393ae1621b7ecd82cb3459e))
* **robots:** [#10094](http://redmine.smartbase.sk/issues/10094) move robots.txt from nginx to django and add sitemaps to obots.txt ([b6c371b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b6c371bc0a023bd71e2bb8c10c979888d20b74c5))
* discount badge conditional from value ([dc6264c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/dc6264c5d2a227b3c13820979d14b9ac359eb204))
* elastic alias per product division ([2022dd5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2022dd5ba6ec12ba9b9216f12735f8f77e3171b0))
* price discount percentage in elastic data without db query ([c31d94f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c31d94ffdf7689d157d8849d92584c97491f52ae))
* product division generic relation ([0f4e8f8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0f4e8f8ccd1754bef52d805bbd8d15bd8d89398a))
* product divisions models ([ea091f8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ea091f84c95520064bc5768cf9e91a45b3bc2625))
* romanian, hungarian .po files ([25e4f8f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/25e4f8fbcb45ffeba7518c4b3f51be108e561ba3))
* **purchase:** [#9761](http://redmine.smartbase.sk/issues/9761) change site to site_alias on purchase model, switch current seller company based on site alias ([f37fb57](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f37fb577f72e214dbbb429d03cfcde316951efab))


### Bug Fixes

* [#9762](http://redmine.smartbase.sk/issues/9762) fix generate dummy tags ([e434e07](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e434e07783969b922895804af0ab9ade1c2356dc))
* [#9776](http://redmine.smartbase.sk/issues/9776) CMS pages hreeflang resolving temporarly moved to project ([6c20617](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6c206178e881a1ea75bba3307e260a42ca137bf6))
* add is_global to preference in template ([f86702b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f86702b542fb542a6dcc11003d0e3d02b8776211))
* add missing if condition when user come first time ([98f8d6d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/98f8d6dea00d90261d8cd584adfeb4026b961752))
* alias must be set on user, even default and raise ([5ce69a0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5ce69a00bf1068fd667bbfd6bf2fa004f6010c2f))
* breadcrumb category feed ([4b627ac](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4b627ac385655a62727161780b8c7c4834268a5d))
* category in detail ecommerce path ([5744ab4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5744ab460e93204121be6bf4efe118a20fec8ea9))
* fix additions stacks info ([2a69fc7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2a69fc721c5f5bf825432cdb65fbb744cf68cd74))
* fix basket due to group by parent ([80665fa](https://gitlab.smartbase.sk/dev/django_smartshop/commit/80665fa28c5820483b602a701409479ffafb0fcc))
* fix basket due to group by parent ([6541f56](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6541f5640c52daa16e10cd2cd5db944825d62170))
* fix configurator import due to empty columns ([92ad1ca](https://gitlab.smartbase.sk/dev/django_smartshop/commit/92ad1ca5eb6bfc53c2ed11a2a6d3268f51177a61))
* fix get group values for product from es ([0594774](https://gitlab.smartbase.sk/dev/django_smartshop/commit/059477411b282c7e141a1776a248afbe84fd12ac))
* fix get group values for product from es ([2a8d0fd](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2a8d0fde489292eebb56c0c98257de5cd232fb62))
* fix get group values for product from es ([2fd0c5d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2fd0c5dde3b2859924bb296527eafd7eeb5ca51f))
* fix import ([ea48f73](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ea48f733656ef2309640023b22ff65d274af54f4))
* fix jinja translations ([adc5ff8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/adc5ff8c99bc2ecfab593994e16c516476228872))
* fix offer variant selection ([49f9da0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/49f9da0457ab632b6fc5f205174109623eaf0d9e))
* fix offer variant style ([b3fb3ed](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b3fb3eda6a0bb16acd789e09901052dbe15cdbb5))
* fix old basket remove ([b6a9dcd](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b6a9dcd8cfdd87400f7325d7bbc185ac52fab11a))
* fix prices in dataLayer ([2bdfec6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2bdfec64ed50a29417db431cd8bc49b33ffaca5c))
* fix refresh placeholder task ([2733e2a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2733e2a151a747d02070416056a46a2fbc9b6238))
* fix seller shop store select modal ([dbb0aed](https://gitlab.smartbase.sk/dev/django_smartshop/commit/dbb0aed193b677d20a5614e845f5288ddde142b0))
* fix sitemap generation ([0da053c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0da053c698943ee0a42f7483b56b46a8110806d2))
* fix vue due to new django cms ([8fd4ebf](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8fd4ebf1c9dde74b750d5dc9c36f209e15853cb3))
* fixes after core merge with tempo ([c73f1fe](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c73f1fe0f85da045a7a4345d68dafd2d57891689))
* line endings to LF ([c4e32a5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c4e32a51037d7b05fbbac24cfb0089faaec4c3d1))
* order html layout for sellers, notificationjs, mailer and purchase process validation ([57c6cdd](https://gitlab.smartbase.sk/dev/django_smartshop/commit/57c6cdd57b5bc2fe1f70f4cecb748ce5605c65e4))
* **catalog:** [#9877](http://redmine.smartbase.sk/issues/9877) fix wishlist prices error ([9fa975c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9fa975c744680675f07a765730d2045e738d9721))
* **catalog:** fixed scroll in catalog after returning from product detail for apple devices ([019b007](https://gitlab.smartbase.sk/dev/django_smartshop/commit/019b0071296b6f0438c62a320fbb6cb82d984b5b))
* **catalog:** product detail object select for current language ([0b5945a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0b5945a79f52ee08246a2b9c1e02978782693064))
* **exponea:** [#10738](http://redmine.smartbase.sk/issues/10738) add missing session into fake request ([dd435b8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/dd435b85ab563db913397f94d9ff4522c7a4d7b2))
* logger in default currency ([c6bf902](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c6bf90294417bea17d8dc29c960ffdca2b0060b4))
* **exponea:** track session_id insted cookie ([fe75122](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fe751223e12d85e14720ba9847c5910f9ac255a2))
* **mailer:** send mails in different languages ([4ab0261](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4ab0261439a405023f2f6476ef3a1c8ea28609f3))
* **seo:** [#9505](http://redmine.smartbase.sk/issues/9505) fix image sitemap template ([29c31ef](https://gitlab.smartbase.sk/dev/django_smartshop/commit/29c31ef15561e1f6d8aa706b82c847e0d27251a8))
* **sitemap:** relative path and file read (works with sftp) ([aa0d341](https://gitlab.smartbase.sk/dev/django_smartshop/commit/aa0d34178674844d10eeafed3ace32380758060e))
* install jsonfield >=2.1.1,<3 ([bd942ec](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bd942ec1b7ec7fdcfdd8d5bfb9a507ea36725e7b))
* skip init of alias preferences if app is not migrated ([a8301a2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a8301a24bcd9d6bafeb1a5f049eba940b6c4908b))
* update import export commit ([2261847](https://gitlab.smartbase.sk/dev/django_smartshop/commit/22618470c10673da79b4b066d2d1c3c37e6d8db9))
* upgrade openpyxl to 2.6.4 -  ExcelReader error ([6386b99](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6386b99754971e2b60cadd755b867d2af710ec5f))



<a name="0.2.20"></a>
## [0.2.20](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.19...0.2.20) (2020-04)


### Bug Fixes

* add timeouted state processing to gopay ([fc4a627](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fc4a627))
* convert line endings to LF ([3162cff](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3162cff))
* fix attribute ([94cfca4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/94cfca4))
* fix manufacturer catalog pagination ([7c77164](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7c77164))
* fix missing import ([0e8dbbe](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0e8dbbe))
* fix proforma invoices ([7c056ba](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7c056ba))
* fix remove old basket ([aa403c4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/aa403c4))
* gallery thumbnail ([4c817c3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4c817c3))
* none category fix ([525cc3b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/525cc3b))
* sb_migrations ([41c1f5d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/41c1f5d))
* sb_migrations ([84d70f8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/84d70f8))
* sb_migrations ([e0ec870](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e0ec870))
* **gopay:** better status handling ([bca6ad3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bca6ad3))


### Features

* **datalayer:** [#11042](http://redmine.smartbase.sk/issues/11042) do not format price to the locale string when pushed to dataLayer ([d148dd8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d148dd8))
* **gopay:** add logging to gopay ([63f9542](https://gitlab.smartbase.sk/dev/django_smartshop/commit/63f9542))
* **gopay:** log gopay transactions with status ([f73d67f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f73d67f))
* **logging:** logstash integration ([3247b42](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3247b42))
* **profile:** [#10842](http://redmine.smartbase.sk/issues/10842) calendar months localization, translation fixes, format price, pl fuzzy fixes ([32bbcac](https://gitlab.smartbase.sk/dev/django_smartshop/commit/32bbcac))
* **purchase:** [#10459](http://redmine.smartbase.sk/issues/10459) add checker to send unpaid purchase to admins via email ([a8c7477](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a8c7477))
* **seo:** [#10267](http://redmine.smartbase.sk/issues/10267) add meta title to shop store ([1b2a54a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1b2a54a))



<a name="0.2.19"></a>
## [0.2.19](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.18...0.2.19) (2020-03)


### Bug Fixes

* **catalog:** set instance for default category image field ([a403781](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a403781))
* **order-history:** [#10766](http://redmine.smartbase.sk/issues/10766) fixed order history for seller ([05c684c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/05c684c))
* add first name and last name to admin non superuser fields, rounding fix ([39cae13](https://gitlab.smartbase.sk/dev/django_smartshop/commit/39cae13))
* breadcrumb category feed ([463391f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/463391f))
* changed price from incl to excl, rounding ([88c0a67](https://gitlab.smartbase.sk/dev/django_smartshop/commit/88c0a67))
* enlarge psc field for offer to 12 chars ([3415f25](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3415f25))
* enlarge psc field for offer to 12 chars ([c4f1833](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c4f1833))
* filter if seller ([5db8036](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5db8036))
* fix missing catalog when user does not have permission to change cms structure ([c54ecb4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c54ecb4))
* fix tax ratio rounding ([dff7337](https://gitlab.smartbase.sk/dev/django_smartshop/commit/dff7337))
* floating point problem in basket ([34721c4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/34721c4))
* **purchase:** fix for generating proforma invoices from payment parts ([ab2b353](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ab2b353))
* **split:** fixed rounding and translation ([27e4f21](https://gitlab.smartbase.sk/dev/django_smartshop/commit/27e4f21))
* condition fix ([9a7eb9c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9a7eb9c))
* do not include long_delivery in form if anonymous user, [#9948](http://redmine.smartbase.sk/issues/9948) ([b7141ce](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b7141ce))
* extended delivery template fix, trans fix, dyn pref fix, split ration check, rounding fixes ([9b04218](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9b04218))
* price rounding on check ([98c5885](https://gitlab.smartbase.sk/dev/django_smartshop/commit/98c5885))
* quantize before calculate rounding ([4050baa](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4050baa))
* quantize before calculate rounding ([1d78440](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1d78440))
* quantize payment part amount, use amount form instance in essox and gopay ([1f91b32](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1f91b32))
* remove max length, restrict in project ([09bb53d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/09bb53d))
* remove quantize to 5 decimal places ([659496f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/659496f))
* ticket 18550 max length of receipt number, ticket 18551 quantize on basket line ([b8d6fa8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b8d6fa8))
* to_decimal util method, dph round fix, catalog js fix ([d653b7f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d653b7f))
* **offer:** fixed missing house number, postal code and country fields ([00f9727](https://gitlab.smartbase.sk/dev/django_smartshop/commit/00f9727))
* **price:** round prices to 5 decimals -> that is excepted, not more decimals ([289f228](https://gitlab.smartbase.sk/dev/django_smartshop/commit/289f228))
* use hasattr instead of try catch for essoxloan check ([5e8b040](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5e8b040))


### Features

* **optimalization:** added webp support, forced jpg conversion ([dc1e097](https://gitlab.smartbase.sk/dev/django_smartshop/commit/dc1e097))
* **purchase:** [#10556](http://redmine.smartbase.sk/issues/10556) split purchase into payment parts ([2c407cc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2c407cc))
* **seo:** [#10260](http://redmine.smartbase.sk/issues/10260) change manufacturer in h1 on catalog and add current page into meta title and meta description ([441c934](https://gitlab.smartbase.sk/dev/django_smartshop/commit/441c934))
* **seo:** [#10267](http://redmine.smartbase.sk/issues/10267) add meta description fields for shop stores and manufacturers ([4d3370f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4d3370f))
* **seo:** [#10730](http://redmine.smartbase.sk/issues/10730) create global preference for dynx params and ga params for dataLayer ([1946de8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1946de8))
* [#10280](http://redmine.smartbase.sk/issues/10280) add filter by pickup store ([5157210](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5157210))
* [#10280](http://redmine.smartbase.sk/issues/10280) rework of filter on user profile, restricted queriset, filter store pickup ([296288c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/296288c))
* [#10280](http://redmine.smartbase.sk/issues/10280) upgrade queryset ([195c842](https://gitlab.smartbase.sk/dev/django_smartshop/commit/195c842))
* [#10522](http://redmine.smartbase.sk/issues/10522) add active shop store from request to payment part payments ([5f6b4a6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5f6b4a6))
* add _after_handle_log_and_print to execute extra code after payment part creation ([68763ed](https://gitlab.smartbase.sk/dev/django_smartshop/commit/68763ed))
* add is really paid to LOG, admin, credit note fix ([efd6e3f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/efd6e3f))
* add seller to purchase filter ([378a584](https://gitlab.smartbase.sk/dev/django_smartshop/commit/378a584))
* restrict purchase queryset in order view for registered user ([0c738eb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0c738eb))
* **auditlog:** log endpoint causing the change ([ae6c8a2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ae6c8a2))
* **catalog:** [#10256](http://redmine.smartbase.sk/issues/10256) preference if categories are listed in megamenu automatically ([991fce1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/991fce1))
* **catalog:** [#10486](http://redmine.smartbase.sk/issues/10486) add after catalog placeholder ([78c2d22](https://gitlab.smartbase.sk/dev/django_smartshop/commit/78c2d22))
* **migrations:** custom smartbase migrations ([922d9eb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/922d9eb))
* **purchase-process:** [#10523](http://redmine.smartbase.sk/issues/10523) timepicker for delivery date ([f3124c0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f3124c0))
* **seo:** add meta title override into category ([ff68c33](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ff68c33))
* category deepest node call returns default category if there is any,... ([4ac2b5b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4ac2b5b))
* migrations update, materialized view migration, category m2m migration ([da23382](https://gitlab.smartbase.sk/dev/django_smartshop/commit/da23382))
* product categories - M2M through model add ([482ad64](https://gitlab.smartbase.sk/dev/django_smartshop/commit/482ad64))
* **robots:** [#10255](http://redmine.smartbase.sk/issues/10255) move robots.txt to application and add sitemaps into it ([029cb53](https://gitlab.smartbase.sk/dev/django_smartshop/commit/029cb53))


### Performance Improvements

* **admin:** add autocomplete to invoice admin ([2a1bb53](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2a1bb53))


### Reverts

* show always in the same old spot ([b361039](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b361039))



<a name="0.2.18"></a>
## [0.2.18](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.17...0.2.18) (2020-02)


### Bug Fixes

* add first name and last name to admin non superuser fields, rounding fix ([c8fe3f1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c8fe3f1))
* Estimated delivery time texts trans, helper messages, template fixes ([29af851](https://gitlab.smartbase.sk/dev/django_smartshop/commit/29af851))
* **admin:** don't translate technical texts ([a6512ff](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a6512ff))
* **product:** fixed feed to elastic on save ([a9cda04](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a9cda04))
* update import export commit ([74ac9f1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/74ac9f1))
* **store-detail:** fixed loading of catalog ([5aa80c8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5aa80c8))
* add space in shop store template ([aa2058e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/aa2058e))
* do not include long_delivery in form if anonymous user, [#9948](http://redmine.smartbase.sk/issues/9948) ([93f96e2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/93f96e2))
* **payment:** fix created date serializer, use tz ([6d9e9eb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6d9e9eb))
* **store:** fixed textation ([665ad84](https://gitlab.smartbase.sk/dev/django_smartshop/commit/665ad84))


### Features

* [#6587](http://redmine.smartbase.sk/issues/6587) robot framework tests gitlab CI integration with catalog pagination tests ([fae323a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fae323a))
* add pref for min max split, rounding line and logic ([1979cf1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1979cf1))



<a name="0.2.17"></a>
## [0.2.17](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.16...0.2.17) (2020-01)


### Bug Fixes

* **cms:** fixed bug preventing publish of non cms pages ([7ab62d2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7ab62d2))
* **cms:** fixed bug preventing publish of non cms pages ([8de0df6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8de0df6))
* **payment:** fix created date serializer, use tz ([79a3a22](https://gitlab.smartbase.sk/dev/django_smartshop/commit/79a3a22))
* **slider:** fixed slider style, added center option for button plugin ([5264061](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5264061))
* **slider:** fixed slider style, added center option for button plugin ([b5e2b08](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b5e2b08))
* **store:** fixed textation, space in template, fix created date serializer, use tz ([01261db](https://gitlab.smartbase.sk/dev/django_smartshop/commit/01261db))
* delivery time and offer billing country ([3e5a281](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3e5a281))
* delivery time and offer billing country ([bf61a19](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bf61a19))
* delivery time and offer billing country ([90caa88](https://gitlab.smartbase.sk/dev/django_smartshop/commit/90caa88))
* requirements and purchase price rounding ([9e12962](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9e12962))


### Features

* **admin:** auto assing all permissions to admin group ([66b5f45](https://gitlab.smartbase.sk/dev/django_smartshop/commit/66b5f45))
* **catalog:** allowable custom ordering on product ([6cdbc4d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6cdbc4d))
* [#9673](http://redmine.smartbase.sk/issues/9673) serializer fixes, text field for receipt number, paymentvalidation copy functionality ([c130ef5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c130ef5))
* [#9673](http://redmine.smartbase.sk/issues/9673) serializer fixes, text field for receipt number, paymentvalidation copy functionality ([90373e1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/90373e1))
* [#9681](http://redmine.smartbase.sk/issues/9681) add purchase document number filter ([8fd3523](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8fd3523))
* [#9681](http://redmine.smartbase.sk/issues/9681) add purchase document number filter ([bc5d55a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bc5d55a))
* [#9894](http://redmine.smartbase.sk/issues/9894) is fiscal cash register field added, admin update ([ca2e353](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ca2e353))
* [#9894](http://redmine.smartbase.sk/issues/9894) is fiscal cash register field added, admin update ([e0498ad](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e0498ad))
* **catalog:** order_override ([5f36a4d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5f36a4d))
* **exposition:** [#9606](http://redmine.smartbase.sk/issues/9606) catalog with exposed products in shopstore detail ([f3e5391](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f3e5391))
* **payment:** [#8666](http://redmine.smartbase.sk/issues/8666) essox loan integration ([0cd7ab2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0cd7ab2))
* **purchase:** [#9681](http://redmine.smartbase.sk/issues/9681) add filter for customer name on purchase history ([977f119](https://gitlab.smartbase.sk/dev/django_smartshop/commit/977f119))
* **query_builder:** [#9376](http://redmine.smartbase.sk/issues/9376) added select2 autocomplete to query_builder inputs ([f5a04a2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f5a04a2))
* **synchronize:** [#9525](http://redmine.smartbase.sk/issues/9525) synchronization framework POC, only outgoing push ([441f5c6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/441f5c6))



<a name="0.2.16"></a>
## [0.2.16](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.15...0.2.16) (2019-12)


### Bug Fixes

* add definition to import id fields ([671a4c9](https://gitlab.smartbase.sk/dev/django_smartshop/commit/671a4c9))
* add definition to import id fields ([3bab7b2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3bab7b2))
* add line to purchase ([eef18a7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/eef18a7))
* missing tags ([d9568ae](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d9568ae))
* **catalog:** fixed edge case where package_dims are imported as decimal numbers ([b0b4e4a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b0b4e4a))
* **common:** remove response status methods (response_200, response_400, response_403, response_404, response_500, failure) ([b516a30](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b516a30))
* **configurator:** [#9451](http://redmine.smartbase.sk/issues/9451) fixed error if deleting option from component ([463c066](https://gitlab.smartbase.sk/dev/django_smartshop/commit/463c066))
* **mailer:** add payment_part to context ([5e82ca1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5e82ca1))
* **product_configurator:** allow update of BaseConfigurationItem in import process ([9fb180f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9fb180f))
* **product-card:** [#8764](http://redmine.smartbase.sk/issues/8764) fixed error with missing data from parent ([3e7d890](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3e7d890))
* **product-item-search:** missing props and other recent changes made to product-card ([331f6aa](https://gitlab.smartbase.sk/dev/django_smartshop/commit/331f6aa))
* **product-item-search:** missing props and other recent changes made to product-card ([fd964f8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fd964f8))
* [#8902](http://redmine.smartbase.sk/issues/8902) remove import ([c46d1ec](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c46d1ec))
* [#8902](http://redmine.smartbase.sk/issues/8902) reset transactions list and count if error catched ([b30e378](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b30e378))
* [#9055](http://redmine.smartbase.sk/issues/9055) add missing days into timedelta ([9629d01](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9629d01))
* [#9235](http://redmine.smartbase.sk/issues/9235) fixes, trans ([c74d664](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c74d664))
* django celery results when connection to db lost ([587c441](https://gitlab.smartbase.sk/dev/django_smartshop/commit/587c441))
* **purchase_process:** delivery_day_offset blank true ([48411dc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/48411dc))
* [#9055](http://redmine.smartbase.sk/issues/9055) add delivery_day_offset and super call to setup ([5ab8e20](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5ab8e20))
* **service:** [#9235](http://redmine.smartbase.sk/issues/9235) rework for more generic usage ([1346c3f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1346c3f))


### Features

* [#8902](http://redmine.smartbase.sk/issues/8902) add type of transaction to FE, color ([785df26](https://gitlab.smartbase.sk/dev/django_smartshop/commit/785df26))
* [#8902](http://redmine.smartbase.sk/issues/8902) cash register id mixin ([c4d02db](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c4d02db))
* [#8902](http://redmine.smartbase.sk/issues/8902) private overridable method to get cash register id ([a759f05](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a759f05))
* [#8902](http://redmine.smartbase.sk/issues/8902) qs fixes, error handling ([a4f0134](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a4f0134))
* [#8902](http://redmine.smartbase.sk/issues/8902) v2 - purchase payments rework ([7ca5d23](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7ca5d23))
* [#89020](http://redmine.smartbase.sk/issues/89020) API serializers and validation wrapper, pokladna ORM select and insert WIP ([3f6777d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3f6777d))
* add permission to users with admin group on app start ([4d4e6be](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4d4e6be))
* HidePluginMixin for CMS Plugins ([5ceeaae](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5ceeaae))
* new API pagination class, views, urls ([0b1d6d3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0b1d6d3))
* redis cluster implementation for django-redis-cache ([e55efcf](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e55efcf))
* redis failsafe send command to failsafe server ([758ef8a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/758ef8a))
* sentry for vuejs ([ea0d484](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ea0d484))
* translations ([e9516cf](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e9516cf))
* **button-plugin:** added button plugin ([46a7422](https://gitlab.smartbase.sk/dev/django_smartshop/commit/46a7422))
* **cash_register:** [#8902](http://redmine.smartbase.sk/issues/8902) cash register model, views WIP ([1bab64d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1bab64d))
* **cash_register:** [#8902](http://redmine.smartbase.sk/issues/8902) move functionality to project, keep abstract views ([dc71a06](https://gitlab.smartbase.sk/dev/django_smartshop/commit/dc71a06))
* **cash-registers:** [#8902](http://redmine.smartbase.sk/issues/8902) template, style, js and translations ([90036d4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/90036d4))
* **cash-registers:** [#9467](http://redmine.smartbase.sk/issues/9467) transactions list with pagination ([4167eff](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4167eff))
* **catalog:** [#8764](http://redmine.smartbase.sk/issues/8764) variants in tile (not grouped in list) ([37fac04](https://gitlab.smartbase.sk/dev/django_smartshop/commit/37fac04))
* **catalog:** [#9522](http://redmine.smartbase.sk/issues/9522) add base implementation for shortest delivery time for product detail ([79b7a0b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/79b7a0b))
* **mailer:** [#9458](http://redmine.smartbase.sk/issues/9458) shop_store email added as cc for purchase emails for shop ([b6627ff](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b6627ff))
* **payment:** [#9235](http://redmine.smartbase.sk/issues/9235) implement internal wire and cod for payments ([c877e51](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c877e51))
* **product-detail:** [#9578](http://redmine.smartbase.sk/issues/9578) added modal with list of store in which is product in stock ([41728e5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/41728e5))
* **purchase:** [#9055](http://redmine.smartbase.sk/issues/9055) add estimated delivery time for purchase process, purchase and printout pdf ([2df9cf7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2df9cf7))
* **purchase:** allow editing of order before processing state ([907a2c6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/907a2c6))
* **purchase_process:** [#9298](http://redmine.smartbase.sk/issues/9298) add overridable method for additional changes, sale type methods, add block ([ebbc148](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ebbc148))
* **purchaseprocess:** [#9434](http://redmine.smartbase.sk/issues/9434) change text and add translations ([9f3ed67](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9f3ed67))
* optimization - enable page cache, django messages from ajax, hook every submit to user cookies csrftoken ([24b8eb2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/24b8eb2))
* **rules:** [#9074](http://redmine.smartbase.sk/issues/9074) create rules engine ([688a08a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/688a08a))
* [#9055](http://redmine.smartbase.sk/issues/9055) WIP FE ([c18ae9b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c18ae9b))


### Performance Improvements

* font display swap ([423f931](https://gitlab.smartbase.sk/dev/django_smartshop/commit/423f931))
* jsi18n cache ([2355ad5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2355ad5))
* lazysizes and lazyload script ([7bc008c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7bc008c))
* lazysizes for background image ([fe91569](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fe91569))



<a name="0.2.15"></a>
## [0.2.15](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.14...0.2.15) (2019-11)


### Bug Fixes

* **product-card:** [#8764](http://redmine.smartbase.sk/issues/8764) fixed error with missing data from parent ([29ec241](https://gitlab.smartbase.sk/dev/django_smartshop/commit/29ec241))
* **shop-stores:** [#9361](http://redmine.smartbase.sk/issues/9361) fix for abstract classes, empty fields in str methods and absolute url ([09154e4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/09154e4))
* remove send page view false ([a6f133b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a6f133b))
* **basket:** [#9205](http://redmine.smartbase.sk/issues/9205) copy configurations of basket line ([32cf8e0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/32cf8e0))
* **blog:** fixed pagination ([14fe4c0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/14fe4c0))
* **business-case:** disable loading ([7d0e57a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7d0e57a))
* **catalog:** [#9069](http://redmine.smartbase.sk/issues/9069) fix product class selection (p_class of products_without_keys was excluded) ([acb37c0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/acb37c0))
* **catalog:** fix step of number input ([26f0043](https://gitlab.smartbase.sk/dev/django_smartshop/commit/26f0043))
* **catalog:** in sort has to be int types ([6c67503](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6c67503))
* **mailer:** fix email send, add customer check ([ec94644](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ec94644))
* [#9106](http://redmine.smartbase.sk/issues/9106) replace line ending special characters ([7e5285f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7e5285f))
* bad string formating, use format instead % (case if name contains %, throws error) ([089e9e4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/089e9e4))
* dont send mail if cutomer is anonymous ([ca48816](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ca48816))
* fixes creating purchase through admin ([7feab2b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7feab2b))
* vue value null fix ([9a140cc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9a140cc))
* **payment:** exclude registry_result_array from audit log ([e4e90f1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e4e90f1))
* **payment:** move registrations to if is registered block due to overrides ([b5e2d70](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b5e2d70))


### Features

* **admin:** added correct location geohash to feed [#7378](http://redmine.smartbase.sk/issues/7378) ([f32bddb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f32bddb))
* **admin:** kibana purchase graphs restricted for seller stores [#7378](http://redmine.smartbase.sk/issues/7378) ([211d01d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/211d01d))
* **analytics:** split analytics tracking into user analytics and seller analytics ([f5b720b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f5b720b))
* **catalog:** [#8764](http://redmine.smartbase.sk/issues/8764) variants in tile (not grouped in list) ([aae2f91](https://gitlab.smartbase.sk/dev/django_smartshop/commit/aae2f91))
* **catalog:** [#9066](http://redmine.smartbase.sk/issues/9066) write product into dataLayer after change product on detail via API ([c6be19d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c6be19d))
* **delivery-service:** [#9337](http://redmine.smartbase.sk/issues/9337) delivery service api ([d3d0627](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d3d0627))
* **heureka:** [#9001](http://redmine.smartbase.sk/issues/9001) do not export products which are not visible to clients to heureka feed ([b2b5e86](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b2b5e86))
* **heureka:** [#9001](http://redmine.smartbase.sk/issues/9001) do not send heureka questionnaire if purchase is not online, e.g. seller purchase ([1d9c899](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1d9c899))
* **importer:** [#9391](http://redmine.smartbase.sk/issues/9391) add old price into catalog importer ([b07db17](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b07db17))
* **product-detail:** [#9337](http://redmine.smartbase.sk/issues/9337) show delivery info ([c4494dc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c4494dc))
* added hungarian translations ([4236c44](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4236c44))
* **payment:** add privilege to superuser to cancel payment ([669b92d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/669b92d))
* **product-detail:** [#9292](http://redmine.smartbase.sk/issues/9292) added placeholder for link or modal with helptext for configuration ([a709775](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a709775))
* decimal rounding default HALF_ROUND_UP ([9b244bc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9b244bc))
* **purchase:** [#8996](http://redmine.smartbase.sk/issues/8996) discount per line in direct sell for purchase process first step ([ffd83eb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ffd83eb))
* **purchase:** [#9106](http://redmine.smartbase.sk/issues/9106) FE validation, backend validation, textarea validate html, getValidationClass with custom classes ([4a44fb5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4a44fb5))
* **purchase:** add fictive payment log with price 0 when purchase total price is 0 to achieve paid status ([a97849e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a97849e))
* **purchase:** do not track purchase into heureka, criteo and affiliate partners if purchase is created by seller ([ade61a8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ade61a8))
* **purchaseprocess:** [#8943](http://redmine.smartbase.sk/issues/8943) remove leading zero from phone and delivery phone number ([3bf1cad](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3bf1cad))
* **service:** payment, delivery services rework to use Price objects with price levels ([4b664e1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4b664e1))
* **store-locator:** [#8523](http://redmine.smartbase.sk/issues/8523) searching shops in radius of specified location ([58f2790](https://gitlab.smartbase.sk/dev/django_smartshop/commit/58f2790))
* **tracking:** fix tracking to dataLayer when product is changed via API ([3a02df7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3a02df7))
* added control to mounted drives on sb-health-check ([e859dea](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e859dea))
* added control to mounted drives on sb-health-check ([8cd6cc1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8cd6cc1))
* decimal rounding default HALF_ROUND_UP ([f4e9f94](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f4e9f94))



<a name="0.2.14"></a>
## [0.2.14](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.13...0.2.14) (2019-10)


### Bug Fixes

* change post_office for forked package ([040430e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/040430e))
* **basket:** fixed error with submitting empty voucher ([4d0264e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4d0264e))
* **catalog:** [#8938](http://redmine.smartbase.sk/issues/8938) is_authenticated fix ([a6e16dc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a6e16dc))
* **catalog:** filter distinct categories in url converter ([b987321](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b987321))
* **catalog:** ordered_dimensions_list padding added ([f1421c0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f1421c0))
* **heureka:** [#9001](http://redmine.smartbase.sk/issues/9001) fix elastic for fetching products to heureka xml ([8a6378b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8a6378b))
* **ms-edge:** removed unsupported Promise finally ([363c30e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/363c30e))
* **payment:** [#8900](http://redmine.smartbase.sk/issues/8900) remove bypass of type CASH ([fc2a054](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fc2a054))
* **product-detail:** [#8828](http://redmine.smartbase.sk/issues/8828) added missing widget type ([e35b0a3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e35b0a3))
* **purchase:** replace true with pass, sloving automated state passing to CASH state ([d869208](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d869208))
* **purchase_processs:** NoneType fix ([5727579](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5727579))
* **purchase-process:** delivery None value fixed ([f827fae](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f827fae))
* arrow function in base template caused non working page on ie ([837d15d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/837d15d))
* base configuration text replace __ with - ([0e09fdd](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0e09fdd))
* exc info in error log for part creation ([21ffce6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/21ffce6))
* generate proforma invoices for all types of payment parts instances except COD service type ([871ca58](https://gitlab.smartbase.sk/dev/django_smartshop/commit/871ca58))
* **basket:** fixed final price in basket if basket is empty and has already some service ([3504e5e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3504e5e))
* **catalog:** [#8585](http://redmine.smartbase.sk/issues/8585) use ID as key ([ccc425d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ccc425d))
* **purchase:** use GET for request query params ([3c7aef1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3c7aef1))
* **purchase-process:** fixed bug where changes in basket lines caused error ([95e9eb2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/95e9eb2))
* Exclude config in rsync ES ([437e03a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/437e03a))
* total by parent + total in manufacturer filter ([15085c7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/15085c7))
* **puchase-process:** [#8753](http://redmine.smartbase.sk/issues/8753) fixed deliveri service filtering ([d63610f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d63610f))
* **search:** [#7380](http://redmine.smartbase.sk/issues/7380) add _doc to DELETE index ([6f4fd08](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6f4fd08))
* **search:** remove deprecated _type in convert_hit_to_template method ([19f6cef](https://gitlab.smartbase.sk/dev/django_smartshop/commit/19f6cef))
* **service:** [#8642](http://redmine.smartbase.sk/issues/8642) add cash type to process ([8b44c08](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8b44c08))
* **service:** [#8642](http://redmine.smartbase.sk/issues/8642) comments ([0336cc2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0336cc2))
* **service:** fix exclude_internal_services condition ([0411586](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0411586))
* **vagrant:** added workaround for vagrant installation fail ([79aeeda](https://gitlab.smartbase.sk/dev/django_smartshop/commit/79aeeda))
* [#7380](http://redmine.smartbase.sk/issues/7380) remove after post generation from ProductFactory ([f4ea5ef](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f4ea5ef))
* collection filters - wrong redirect fix ([6d78f9d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6d78f9d))
* elasticsearch alias fix ([0d72b07](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0d72b07))
* install sh ES 7.3.2 fix ([5b1a2cb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5b1a2cb))
* KibanaDashboardView iframe_src fix ([53c2f9b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/53c2f9b))
* remove comments ([9f4922f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9f4922f))
* url ([65b6907](https://gitlab.smartbase.sk/dev/django_smartshop/commit/65b6907))


### Features

* **admin:** [#8672](http://redmine.smartbase.sk/issues/8672) allow adding more than one AOG values in product variants edit view ([631f7ee](https://gitlab.smartbase.sk/dev/django_smartshop/commit/631f7ee))
* **admin:** link basket line to product detail ([d561be7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d561be7))
* **catalog:** [#7483](http://redmine.smartbase.sk/issues/7483) add user groups into catalog cache_key ([0011e89](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0011e89))
* **catalog:** [#8536](http://redmine.smartbase.sk/issues/8536) product detail page renders colors variants up to 4 color and icons per variant ([21e1b2b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/21e1b2b))
* **catalog:** [#8654](http://redmine.smartbase.sk/issues/8654) scroll to previous position in catalog ([8a12193](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8a12193))
* **catalog:** [#8654](http://redmine.smartbase.sk/issues/8654) scroll to previous position in catalog after returning from other page ([1228b2a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1228b2a))
* **common:** [#8983](http://redmine.smartbase.sk/issues/8983) add sb_seller into cookie if seller is logged in ([b0bb438](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b0bb438))
* **heureka:** [#8751](http://redmine.smartbase.sk/issues/8751) add item ids to heureka questionnaire ([f3ff839](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f3ff839))
* **marketing:** improved landing page generator plugin [#6278](http://redmine.smartbase.sk/issues/6278) ([f2d4150](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f2d4150))
* **modal:** [#8648](http://redmine.smartbase.sk/issues/8648) added modal plugin with video plugin support ([b3e83dd](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b3e83dd))
* **purchase:** [#7910](http://redmine.smartbase.sk/issues/7910) add filtering for order history ([4da2073](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4da2073))
* **purchase:** [#7910](http://redmine.smartbase.sk/issues/7910) order history pagination and search connection ([aa66dff](https://gitlab.smartbase.sk/dev/django_smartshop/commit/aa66dff))
* **purchase:** [#7910](http://redmine.smartbase.sk/issues/7910) rewrite order history from django template to rest api ([1368361](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1368361))
* **purchase:** [#8604](http://redmine.smartbase.sk/issues/8604) added filter to show all orders in shop for seller ([b0b1351](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b0b1351))
* **purchase:** [#8704](http://redmine.smartbase.sk/issues/8704) create voucher overridable and add some method for calculating prices for various users ([1db290b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1db290b))
* **purchase:** [#8983](http://redmine.smartbase.sk/issues/8983) add store_name variable into dataLayer ([0291be5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0291be5))
* **purchase:** add filter to purchase for seller ([e9fdbaf](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e9fdbaf))
* **service:** add filter_qs_by_sale_type, rework serializers, remove is_input_user_seller ([6a62807](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6a62807))
* **service:** add service groups, serializer fix by ([f778a59](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f778a59))
* **shopping-cart:** [#8996](http://redmine.smartbase.sk/issues/8996) added option to apply line discounts in direct sell ([bc2a722](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bc2a722))
* [#8647](http://redmine.smartbase.sk/issues/8647) add AttributeOptionGroupSet ([49dce9c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/49dce9c))
* [#8906](http://redmine.smartbase.sk/issues/8906) User Reviews plugin ([56b769c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/56b769c))
* **search:** [#7380](http://redmine.smartbase.sk/issues/7380) WIP elasticsearch 7.3.2 ([b6c3f54](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b6c3f54))
* **search:** ngram min max correction ([062d8b2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/062d8b2))
* **service:** [#8642](http://redmine.smartbase.sk/issues/8642) add cash type to payment service ([fff2bac](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fff2bac))
* **service:** [#8642](http://redmine.smartbase.sk/issues/8642) comment for numbering ([44805b0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/44805b0))
* **shop_stores:** [#8750](http://redmine.smartbase.sk/issues/8750) opening hours template, serializer, method for all, context updates ([286edad](https://gitlab.smartbase.sk/dev/django_smartshop/commit/286edad))
* **shop_stores:** add default (eshop) store ([6ad1b2b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6ad1b2b))
* **shopstore-detail:** [#8645](http://redmine.smartbase.sk/issues/8645) shopstore detail ([8c2d834](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8c2d834))
* **social:** add middleware to catch social auth exceptions ([c5a2c1e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c5a2c1e))
* [#7380](http://redmine.smartbase.sk/issues/7380) add to etc kibana and ealstic for vagrant (v 7.3.2) ([c33fac3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c33fac3))
* [#7380](http://redmine.smartbase.sk/issues/7380) WIP es upgrade part 2 ([537c0fd](https://gitlab.smartbase.sk/dev/django_smartshop/commit/537c0fd))
* add postgresql-11 to install sh ([d71ae66](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d71ae66))
* optimize catalog load from es ([cc505bf](https://gitlab.smartbase.sk/dev/django_smartshop/commit/cc505bf))



<a name="0.2.13"></a>
## [0.2.13](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.12...0.2.13) (2019-09)


### Bug Fixes

* **catalog:** [#8585](http://redmine.smartbase.sk/issues/8585) rename const ([91fa87d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/91fa87d))
* [#8282](http://redmine.smartbase.sk/issues/8282) handle None purchase in payment creation ([fd16092](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fd16092))
* [#8282](http://redmine.smartbase.sk/issues/8282) registration moved outside if  condition ([af45b10](https://gitlab.smartbase.sk/dev/django_smartshop/commit/af45b10))
* [#8432](http://redmine.smartbase.sk/issues/8432) condition if payment part instance is None ([497e777](https://gitlab.smartbase.sk/dev/django_smartshop/commit/497e777))
* [#8432](http://redmine.smartbase.sk/issues/8432) remove unused field card_number ([ad31eeb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ad31eeb))
* [#8489](http://redmine.smartbase.sk/issues/8489) fix mail tempalte, remove wire instructions mail ([cff4f70](https://gitlab.smartbase.sk/dev/django_smartshop/commit/cff4f70))
* [#8489](http://redmine.smartbase.sk/issues/8489) is_online_purchase property fix ([d527ded](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d527ded))
* admin product filter fix, remove quantize on service price, price formating ([a5b7519](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a5b7519))
* basket share template fix ([9f2f195](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9f2f195))
* cookie middleware legacy ([7f9e4ba](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7f9e4ba))
* filter distinct categories in url converter ([d9c72bc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d9c72bc))
* fix affiliate middleware after MR ([acd73c5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/acd73c5))
* fix imports after MR ([cedefac](https://gitlab.smartbase.sk/dev/django_smartshop/commit/cedefac))
* fix settings after merge from production 2.1 ([ecde393](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ecde393))
* include purchases for sellers in invoice API ([013c725](https://gitlab.smartbase.sk/dev/django_smartshop/commit/013c725))
* new commit for import export ([411cd17](https://gitlab.smartbase.sk/dev/django_smartshop/commit/411cd17))
* pagination in catalog when using range slider ([802697c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/802697c))
* price formatting ([e9cdc7e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e9cdc7e))
* PurchaseQuerySetMixin and class methods for purchase selection ([0c7f776](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0c7f776))
* remove MobileMenuItemPlugin from dummy ([14a9ef6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/14a9ef6))
* remove script for ahoj calculator ([0356280](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0356280))
* restriction method used in admin, add qs for superuser ([9082a93](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9082a93))
* select user profile for purchase ny email of customer ([62ca725](https://gitlab.smartbase.sk/dev/django_smartshop/commit/62ca725))
* shipping and payment template payment price format fix ([27c3921](https://gitlab.smartbase.sk/dev/django_smartshop/commit/27c3921))
* update commit for import export ([a96f35c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a96f35c))
* **admin:** file generation in graph view of purchase process ([bad19c0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bad19c0))
* **catalog:** [#7870](http://redmine.smartbase.sk/issues/7870) fix filter color tooltips ([80b7b03](https://gitlab.smartbase.sk/dev/django_smartshop/commit/80b7b03))
* use SB fork ([4a24e51](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4a24e51))
* user profile filtering condition fix ([1b93b4e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1b93b4e))
* vertical align colour filter ([dca1a01](https://gitlab.smartbase.sk/dev/django_smartshop/commit/dca1a01))
* **affiliate:** [#7885](http://redmine.smartbase.sk/issues/7885) fix tests ([9f9a63a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9f9a63a))
* **affiliate:** [#7885](http://redmine.smartbase.sk/issues/7885) remove StaticPlaceholder from cacheops ([da423de](https://gitlab.smartbase.sk/dev/django_smartshop/commit/da423de))


### Features

* **catalog:** [#8585](http://redmine.smartbase.sk/issues/8585) attribute filtering by ID, constance, JS ([6a4f38a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6a4f38a))
* add vagrant db user as superuser ([6013a2d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6013a2d))
* **admin:** kibana dashboard integration ([d0a9fe3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d0a9fe3))
* **business_case:** [#7915](http://redmine.smartbase.sk/issues/7915) add offers_simple endpoint ([02f1ca3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/02f1ca3))
* **business_case:** [#7915](http://redmine.smartbase.sk/issues/7915) add server pagination to listing api ([4db053a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4db053a))
* **business_case:** [#7915](http://redmine.smartbase.sk/issues/7915) add server side filtering and ordering of business cases ([44267ca](https://gitlab.smartbase.sk/dev/django_smartshop/commit/44267ca))
* **business_case:** [#7915](http://redmine.smartbase.sk/issues/7915) change paginator from LimitOffset to PageNumber ([c90a198](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c90a198))
* **business-case:** [#7915](http://redmine.smartbase.sk/issues/7915) connection of offers_simple ([28a4be6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/28a4be6))
* **business-case:** connection of pagination and filtering ([305488e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/305488e))
* [#8432](http://redmine.smartbase.sk/issues/8432) getting proforma invoice not depended on service type, add service field to admin ([e8a5006](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e8a5006))
* [#8459](http://redmine.smartbase.sk/issues/8459) added plugin for raw html code and css ([654e690](https://gitlab.smartbase.sk/dev/django_smartshop/commit/654e690))
* **catalog:** [#7483](http://redmine.smartbase.sk/issues/7483) add auth.Group on product ([dde5047](https://gitlab.smartbase.sk/dev/django_smartshop/commit/dde5047))
* **catalog:** [#7483](http://redmine.smartbase.sk/issues/7483) fix exceptions ([3b51087](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3b51087))
* **catalog:** [#7483](http://redmine.smartbase.sk/issues/7483) products auth.Group visibility ([0d1b0fc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0d1b0fc))
* [#8390](http://redmine.smartbase.sk/issues/8390) add last name of customer to order history, update qs of purchases ([0dbad27](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0dbad27))
* [#8390](http://redmine.smartbase.sk/issues/8390) seller/superuser condition to show lines in order history ([ee931ce](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ee931ce))
* [#8489](http://redmine.smartbase.sk/issues/8489) WIP new mail for wire instructions, is_online_purchase property for purchase ([e2168bc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e2168bc))
* [#8490](http://redmine.smartbase.sk/issues/8490) add is_internal_service to services, update serializers, qs restrictions ([5343a3b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5343a3b))
* [#8523](http://redmine.smartbase.sk/issues/8523) store locator address broken to separate fields, added towns filter, style adjustements ([55d3fda](https://gitlab.smartbase.sk/dev/django_smartshop/commit/55d3fda))
* [#8539](http://redmine.smartbase.sk/issues/8539) fixed header navigation ([fba50e5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fba50e5))
* **affiliate:** [#7885](http://redmine.smartbase.sk/issues/7885) create admin for affiliate partners ([88a5081](https://gitlab.smartbase.sk/dev/django_smartshop/commit/88a5081))
* **affiliate:** [#7885](http://redmine.smartbase.sk/issues/7885) create register purchase script for affiliate partners ([07b0ef5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/07b0ef5))
* **affiliate:** [#8181](http://redmine.smartbase.sk/issues/8181) implement better handling of affiliate partners ([f2dd3c9](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f2dd3c9))
* **analitic:** [#8208](http://redmine.smartbase.sk/issues/8208) add ecommerce tracking into checkout process ([fd7c864](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fd7c864))
* **business_case:** [#8285](http://redmine.smartbase.sk/issues/8285) seller discount url only for seller ([a6eb679](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a6eb679))
* **catalog:** [#7870](http://redmine.smartbase.sk/issues/7870) do not shop filter with one option if not necessary ([8877596](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8877596))
* **catalog:** [#8240](http://redmine.smartbase.sk/issues/8240) add shipping promotion template into block ([0dc74f3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0dc74f3))
* **catalog:** [#8251](http://redmine.smartbase.sk/issues/8251) scroll to opening position after closing product description tab on mobile ([daddaa6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/daddaa6))
* **catalog:** [#8455](http://redmine.smartbase.sk/issues/8455) add default image to color selection of product variant ([c7df69b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c7df69b))
* **catalog:** [#8481](http://redmine.smartbase.sk/issues/8481) add missing colon ([8f7d878](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8f7d878))
* **customer:** [#7260](http://redmine.smartbase.sk/issues/7260) send copy of contact form email to also to customer ([1c0def2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1c0def2))
* **customer:** [#8244](http://redmine.smartbase.sk/issues/8244) add block newsletter_inputs to newsletter alternative ([364fd77](https://gitlab.smartbase.sk/dev/django_smartshop/commit/364fd77))
* **marketing:** [#8400](http://redmine.smartbase.sk/issues/8400) create criteo dataLayer ([1bc4172](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1bc4172))
* **marketing:** [#8400](http://redmine.smartbase.sk/issues/8400) move criteo datalayer into separate files ([99778b2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/99778b2))
* **purchase:** [#7374](http://redmine.smartbase.sk/issues/7374) FE sort of delivery service ([87429bc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/87429bc))
* **purchase:** [#8285](http://redmine.smartbase.sk/issues/8285) move seller discount to separate endpoint ([b5c80ec](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b5c80ec))
* **purchase:** [#8375](http://redmine.smartbase.sk/issues/8375) add shiping and payment price including tax ([6df86a1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6df86a1))
* changed profile history to use values_list [#7910](http://redmine.smartbase.sk/issues/7910) ([84d1608](https://gitlab.smartbase.sk/dev/django_smartshop/commit/84d1608))
* confirmation dialog implementation ([35ab415](https://gitlab.smartbase.sk/dev/django_smartshop/commit/35ab415))
* save ralation to parent object in log entry, admin qs adn formset ([113149d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/113149d))
* WIP audit log for purchase ([15b8583](https://gitlab.smartbase.sk/dev/django_smartshop/commit/15b8583))


### BREAKING CHANGES

* **business_case:** need to install pg_trgm and unaccent extensions into PgSQL
* **catalog:** User can see and manipulate only with products without auth.Group or with products which has at least one auth.Group the same as user



<a name="0.2.12"></a>
## [0.2.12](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.11...0.2.12) (2019-08)


### Bug Fixes

* [#8011](http://redmine.smartbase.sk/issues/8011) comments, renamings ([8f98dfa](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8f98dfa))
* [#8011](http://redmine.smartbase.sk/issues/8011) quantize total prices ([03d49b2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/03d49b2))
* [#8071](http://redmine.smartbase.sk/issues/8071) if 100 percent deposit do not cast to int ([7d295f4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7d295f4))
* [#8071](http://redmine.smartbase.sk/issues/8071) MR fixes ([d472ab7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d472ab7))
* cookies allow boolean ([c2d1ea0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c2d1ea0))
* correct sort of shop_stores in purchase ([00740c2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/00740c2))
* correct translation of categories ([9bf48ec](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9bf48ec))
* is_authenticated fix (Backwards-compatibility support for using it as a method will be removed in Django 2.0.) ([518048c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/518048c))
* is_cancellation not needed, it is in kwargs allready ([79e450d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/79e450d))
* logger ([5dc2958](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5dc2958))
* payment validation and proforma URL ([e426b02](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e426b02))
* **catalog:** product detail serializer image field - source main_image_url ([10cdf2f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/10cdf2f))
* rewrite asynchronous addition lines to basket into recursion way ([ca6286b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ca6286b))
* set correct actionField in dataLayer event on remove from basket ([9b5ef7e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9b5ef7e))
* set correct exponea tracking parameters ([d67137e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d67137e))
* The order of arguments for API key and username has reversed in 2.1.0 ([f6a733e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f6a733e))


### Features

* [#8006](http://redmine.smartbase.sk/issues/8006) configuration moved to configuration modal added configuration to generatedummy and show images or color in base configuration ([8db5b36](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8db5b36))
* [#8011](http://redmine.smartbase.sk/issues/8011) [#8013](http://redmine.smartbase.sk/issues/8013) pricing summary fixes, exp. rounding implementation, configurator quantize removal ([647cdc0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/647cdc0))
* [#8011](http://redmine.smartbase.sk/issues/8011) voucher price distribution among tax ratios, minor fixes, serializer update ([7237f64](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7237f64))
* [#8071](http://redmine.smartbase.sk/issues/8071) 40 and 100 percent deposit spilt FE BE ([2e65dd2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2e65dd2))
* [#8071](http://redmine.smartbase.sk/issues/8071) cancellation context in invoices (payment validation) ([7450215](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7450215))
* [#8071](http://redmine.smartbase.sk/issues/8071) eKasa cancelation WIP ([72dd252](https://gitlab.smartbase.sk/dev/django_smartshop/commit/72dd252))
* [#8071](http://redmine.smartbase.sk/issues/8071) list in invoice only payment part logs not canceled and not type cancellation, quantize result of round ([27ee2f5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/27ee2f5))
* [#8071](http://redmine.smartbase.sk/issues/8071) save reference object if cancellation ([6296612](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6296612))
* [#8071](http://redmine.smartbase.sk/issues/8071) v2 cancellation context in invoices (payment validation) - used for EET cancellation ([d075370](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d075370))
* **analytics:** [#7469](http://redmine.smartbase.sk/issues/7469) make orderSubmit event changeable in projects ([a20835a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a20835a))
* **analytics:** add mechanisms to track newsletter subscriptions by dataLayer ([545e029](https://gitlab.smartbase.sk/dev/django_smartshop/commit/545e029))
* **basket:** add new datalayer event and fix gtag events on add or remove from basket ([5e08814](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5e08814))
* **catalog:** feed products optimization ([7e4abe8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7e4abe8))
* **consent:** cookie management in background, cookie change signal ([177a518](https://gitlab.smartbase.sk/dev/django_smartshop/commit/177a518))
* **consent:** init impl cookie settings BE ([6dbd55e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6dbd55e))
* **cookies:** cookies management ([d944a50](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d944a50))
* **crm:** added seller type ([e254e3c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e254e3c))
* **search:** order no - partial search ngram ([ca4745a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ca4745a))
* [#7996](http://redmine.smartbase.sk/issues/7996) catalog different languages redirect ([3007ec7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3007ec7))
* added --big-dataset switch to generatedummy, fixed search item after wrapping to product-grouped component and changed product detail query to get stock from main document ([c5a3ccd](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c5a3ccd))
* **stores:** shop store visibility, hide default warehouse ([b156e55](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b156e55))
* **warehouse:** added possibility for stores to act as warehouses, filtering by product ids in these warehouses ([0675fe6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0675fe6))
* [#7777](http://redmine.smartbase.sk/issues/7777) added external stock functionality if EXTERNAL_STOCK_URL is provided ([19139fc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/19139fc))
* [#7949](http://redmine.smartbase.sk/issues/7949) pricing summary upgrade, template blocks, document number usage, delivery date,  fix invoice item lines, show prices without discount, minor fixes, replace purchase number with document number,  invoice total template fixes, remove is_invoice condition, css ([e0cdd94](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e0cdd94))
* **warehouse:** added possibility for stores to act as warehouses, filtering by product ids in these warehouses ([c5c754f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c5c754f))


### Performance Improvements

* [#7962](http://redmine.smartbase.sk/issues/7962) update stock performance changes ([cbd2749](https://gitlab.smartbase.sk/dev/django_smartshop/commit/cbd2749))
* feed performance changes ([57e3134](https://gitlab.smartbase.sk/dev/django_smartshop/commit/57e3134))



<a name="0.2.11"></a>
## [0.2.11](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.10...0.2.11) (2019-07)


### Bug Fixes

* [#7767](http://redmine.smartbase.sk/issues/7767) add Total amout to print out ([65c6d2a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/65c6d2a))
* add name of option to base configuration js ([3f06954](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3f06954))
* add overridable mthod to get purchase form self ([962ecbb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/962ecbb))
* add utils method set_user_currency ([30e8267](https://gitlab.smartbase.sk/dev/django_smartshop/commit/30e8267))
* Change invoicing file permmission ([ee4336d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ee4336d))
* decrease price health check redis key expiration ([9412082](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9412082))
* do not include payment parts in payment validation, only one line per payment validation ([f0230be](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f0230be))
* extend AbstractDocumentModelTemplate, serial no. generation, fix delivery service in offer ([60cec03](https://gitlab.smartbase.sk/dev/django_smartshop/commit/60cec03))
* filter price defnition by weight AND dimension, return default price if no definition matches the query ([05402f0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/05402f0))
* fix payment part nubering, fix v-fi in pp template for delivery ([df852bf](https://gitlab.smartbase.sk/dev/django_smartshop/commit/df852bf))
* generate proforma for all part is not seller, if seller only for deposit ([498bcd4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/498bcd4))
* minor fixes, activation link, serializer class, offer serach ([4bf18ef](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4bf18ef))
* payment validation, printout, proforma invoice, invoice generation ([a15fcd9](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a15fcd9))
* return None if no definition matched ([730c6c8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/730c6c8))
* shop stores app fix ([c5bbb7d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c5bbb7d))
* upgrade grouping by attribute option functionality ([13e7ba7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/13e7ba7))
* use is_direct_sale ([a71e513](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a71e513))


### Features

* [#7482](http://redmine.smartbase.sk/issues/7482) added API endpoing to return base price of atyp based on provided configuration ([038e427](https://gitlab.smartbase.sk/dev/django_smartshop/commit/038e427))
* order history in account ordered by timestamp created ([c815433](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c815433))
* restrict queryset if user is seller, add change list filter for shop store ([528b789](https://gitlab.smartbase.sk/dev/django_smartshop/commit/528b789))
* **order-history:** [#7859](http://redmine.smartbase.sk/issues/7859) pagination for order history ([57cc679](https://gitlab.smartbase.sk/dev/django_smartshop/commit/57cc679))
* [#7482](http://redmine.smartbase.sk/issues/7482) a-types initial commit ([ded7a7b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ded7a7b))
* [#7482](http://redmine.smartbase.sk/issues/7482) added sql to get price based on user and currency ([b6830d8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b6830d8))
* [#7482](http://redmine.smartbase.sk/issues/7482) basic export and import for atype items ([d84e348](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d84e348))
* add allowed payments to constances to define payment management availability ([6a6b46a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6a6b46a))
* add is_allowed_for_payment_split to payment service ([b30e423](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b30e423))
* added monkeypatch to write in sitemap generator ([fff7c06](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fff7c06))
* added prerender health check ([f77c345](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f77c345))
* generate payment services by code name (cash and card for internal usage in payment parts), kwarg for file gen., doc gen fix ([fb7404a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fb7404a))
* generating sitemaps for all languages by domain ([9e8d8cc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9e8d8cc))
* printout generation, download link to FE, serialization ([7e4ad9b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7e4ad9b))
* remove printout generation, generate when getting the file ([501b504](https://gitlab.smartbase.sk/dev/django_smartshop/commit/501b504))
* requests timeouts ([30f0be1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/30f0be1))
* **invoice:** translations ([db9b451](https://gitlab.smartbase.sk/dev/django_smartshop/commit/db9b451))



<a name="0.2.10"></a>
## [0.2.10](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.9...0.2.10) (2019-06)


### Bug Fixes

* [#7348](http://redmine.smartbase.sk/issues/7348) typo correction ([80ed8bb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/80ed8bb))
* change commit ID for import_export ([c7af8a2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c7af8a2))
* changed base url for pdf files to also work in wild server env ([233aeda](https://gitlab.smartbase.sk/dev/django_smartshop/commit/233aeda))
* handle invalid dimensions of product ([c084edc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c084edc))
* invoice generation with payment part, invoice tests fix ([7c5696a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7c5696a))
* remove hardcoded SK language code, use first defined language in import proces for parent slug mapping ([6613186](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6613186))
* Show payment management (condition) on order.html ([e1735b9](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e1735b9))


### Features

* **invoice:** added optional shop store invoicing by external_id ([c85bc80](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c85bc80))
* [#6279](http://redmine.smartbase.sk/issues/6279) added block region selector ([360784f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/360784f))
* [#7362](http://redmine.smartbase.sk/issues/7362) add constances, part recreation handling, paid state runnable check ([f5007e7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f5007e7))
* [#7362](http://redmine.smartbase.sk/issues/7362) add default seller delivey and payment service, rework splitting process ([e43e448](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e43e448))
* [#7362](http://redmine.smartbase.sk/issues/7362) add inline to admin, additional info field ([534c747](https://gitlab.smartbase.sk/dev/django_smartshop/commit/534c747))
* [#7362](http://redmine.smartbase.sk/issues/7362) change on delete arguments ([36f6178](https://gitlab.smartbase.sk/dev/django_smartshop/commit/36f6178))
* [#7362](http://redmine.smartbase.sk/issues/7362) compatibility fix ([0c074be](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0c074be))
* [#7362](http://redmine.smartbase.sk/issues/7362) create payment object ([24b3284](https://gitlab.smartbase.sk/dev/django_smartshop/commit/24b3284))
* [#7362](http://redmine.smartbase.sk/issues/7362) dyn pref for crm seller payment methods, MR fixes, overridable method for print and log ([d023a78](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d023a78))
* [#7362](http://redmine.smartbase.sk/issues/7362) generate payment validation for deposit and balance ([7367c2a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7367c2a))
* [#7362](http://redmine.smartbase.sk/issues/7362) iframe reload, custom tax ratio, service admin readonly, generate services for seller ([25d6b0d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/25d6b0d))
* [#7362](http://redmine.smartbase.sk/issues/7362) implement balance and deposit ([7e9ee70](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7e9ee70))
* [#7362](http://redmine.smartbase.sk/issues/7362) js event trigger in admin, FK for instance added ([29b2283](https://gitlab.smartbase.sk/dev/django_smartshop/commit/29b2283))
* [#7362](http://redmine.smartbase.sk/issues/7362) move forms, add kwargs for proforma ([8071769](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8071769))
* [#7362](http://redmine.smartbase.sk/issues/7362) move Payment and PaymentPart to separated app ([e64c741](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e64c741))
* [#7362](http://redmine.smartbase.sk/issues/7362) MR comment fixes, serializer, trans, tempalte css ([6e59544](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6e59544))
* [#7362](http://redmine.smartbase.sk/issues/7362) MR resolving, admin restrictions, default tax, deposit amounts, comments, js urls ([e1cd138](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e1cd138))
* [#7362](http://redmine.smartbase.sk/issues/7362) part number field, update invoices, admin, tempalte ([5cf3564](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5cf3564))
* [#7362](http://redmine.smartbase.sk/issues/7362) payment view from admin, template tag fix, provider skip ([f032267](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f032267))
* [#7362](http://redmine.smartbase.sk/issues/7362) PaymentPart implementation ([3b7b0c6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3b7b0c6))
* [#7362](http://redmine.smartbase.sk/issues/7362) remove redundant stuff, add kwargs ([e7dcd5c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e7dcd5c))
* [#7362](http://redmine.smartbase.sk/issues/7362) remove unused link ([cef9c1c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/cef9c1c))
* [#7362](http://redmine.smartbase.sk/issues/7362) seller payment migration from project to core ([7d5eb70](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7d5eb70))
* [#7362](http://redmine.smartbase.sk/issues/7362) update invoice templates, add service to payment part, invoice context update, pricing summary update ([62b7b9a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/62b7b9a))
* [#7362](http://redmine.smartbase.sk/issues/7362) use TimeStampedModel in PayementPart ([8e9961d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8e9961d))
* [#7362](http://redmine.smartbase.sk/issues/7362) validation and proforma per payment part, order tempalte ([8cda126](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8cda126))
* [#7379](http://redmine.smartbase.sk/issues/7379) feeding purchase to ES ([6edf01b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6edf01b))
* [#7404](http://redmine.smartbase.sk/issues/7404) added loader mixin and disabled email field if customer was populated from user_profile, changed disabled input style ([f79d69c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f79d69c))
* [#7405](http://redmine.smartbase.sk/issues/7405) added option to currency and shipping and payment for anonymous user ([8458b3a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8458b3a))
* [#7407](http://redmine.smartbase.sk/issues/7407) added user_profile to customer to be able determine if customer was populated from user_profile and which user_profile is it ([86843a6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/86843a6))
* [#7502](http://redmine.smartbase.sk/issues/7502) frontend for configurator ([b52ab05](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b52ab05))
* 7362 WIP MR comments rewrok, proforma generation, admin ([0ca7672](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0ca7672))
* added business case and CRM package ([e86e968](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e86e968))
* basket middleware moved to core ([cd58624](https://gitlab.smartbase.sk/dev/django_smartshop/commit/cd58624))
* Django 2.1 upgrade (on_delete added) ([f13cbe2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f13cbe2))
* freeze upgraded dependencies ([bf80b44](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bf80b44))
* moved all html, CSS and JS from prospanek ([233c340](https://gitlab.smartbase.sk/dev/django_smartshop/commit/233c340))
* removed django auth function based views ([eb13c12](https://gitlab.smartbase.sk/dev/django_smartshop/commit/eb13c12))
* replaced assigment_tag with simple_tag and list and detail route with action ([e20d2ee](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e20d2ee))
* upgrade to pyton 3.7 and to debian 9 ([9fc3b04](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9fc3b04))
* **catalog:** added external IDs to base catalog models ([79154bb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/79154bb))
* **warehouse:** [#7470](http://redmine.smartbase.sk/issues/7470) multiple producers per warehouse ([6d0dd9f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6d0dd9f))



<a name="0.2.9"></a>
## [0.2.9](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.8...0.2.9) (2019-05)


### Bug Fixes

* fix static placeholder cache ([e0dd764](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e0dd764))
* **catalog:** handle empty category product urls ([ea8f41d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ea8f41d))
* [#7144](http://redmine.smartbase.sk/issues/7144) fixed bad recipeint of contact mail ([b60a05d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b60a05d))
* elasticsearch parse_min_max_price if value None handling ([c489267](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c489267))
* fixed  min and max price rounding ([247cf32](https://gitlab.smartbase.sk/dev/django_smartshop/commit/247cf32))
* **admin:** Purchase autocomplete not available for non-superuser ([71eab50](https://gitlab.smartbase.sk/dev/django_smartshop/commit/71eab50))
* **shipping_calendar:** added short delivery message to fix problem with holidays between delivery dates [#7110](http://redmine.smartbase.sk/issues/7110) ([d45df7e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d45df7e))
* sold count calculation [#5282](http://redmine.smartbase.sk/issues/5282) ([75aa90a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/75aa90a))
* split THUMBNAILS settings ([3333a62](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3333a62))


### Features

* **basket:** allow overriding creation of basket in middleware ([8f1fb5e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8f1fb5e))
* **common:** added generic token generator ([06174cc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/06174cc))
* **exponea:** track customer data ([53b6ba8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/53b6ba8))
* **notification:** [#7005](http://redmine.smartbase.sk/issues/7005) added notification bar plugin to notify eshop ([b96f51f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b96f51f))
* **performance:** new caching for placeholders ([0c6f138](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0c6f138))
* **rest:** added multiserializer utility ([f3c3feb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f3c3feb))
* **section:** [#7018](http://redmine.smartbase.sk/issues/7018) added section plugin to allow users add sections with custom background, borders and spacing options ([8e0ec72](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8e0ec72))
* **store:** [#7146](http://redmine.smartbase.sk/issues/7146) added vue store ([6f27b0a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6f27b0a))
* **store locator:** [#7181](http://redmine.smartbase.sk/issues/7181) added street view embed into gallery and reworked template from standart ([75056d2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/75056d2))
* [#6472](http://redmine.smartbase.sk/issues/6472) added bootstrap grid ([4a6aefd](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4a6aefd))
* [#6472](http://redmine.smartbase.sk/issues/6472) added bootstrap grid ([4d29dc3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4d29dc3))
* [#6472](http://redmine.smartbase.sk/issues/6472) added bootstrap grid ([dbdbacf](https://gitlab.smartbase.sk/dev/django_smartshop/commit/dbdbacf))
* [#6472](http://redmine.smartbase.sk/issues/6472) added bootstrap grid ([82ec8f4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/82ec8f4))
* [#7099](http://redmine.smartbase.sk/issues/7099) option to be able hide filter for some category ([4c249bd](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4c249bd))
* bootstrap 4 grid plugin ([8d638e2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8d638e2))
* bootstrap 4 grid plugin ([f5e18a7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f5e18a7))


### Performance Improvements

* enable pgbouncer in celery -> cursor doesnt exist error fix ([dd13858](https://gitlab.smartbase.sk/dev/django_smartshop/commit/dd13858))


### Reverts

* reverted changes incorectly discarted during rebase ([019c248](https://gitlab.smartbase.sk/dev/django_smartshop/commit/019c248))


### triv

* **settings:** upgrade middleware classes to Django 1.10+ style ([f1fafe0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f1fafe0))


### BREAKING CHANGES

* **settings:** property MIDDLEWAE_CLASSES renamed to MIDDLEWARE



<a name="0.2.8"></a>
## [0.2.8](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.7...0.2.8) (2019-04-30)


### Bug Fixes

* **colorfield:** fixed bug in regex right after colorfield creation ([7412d7f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7412d7f))
* **heureka:** fixes Heureka when using multiple Aliases for same domain [#6761](http://redmine.smartbase.sk/issues/6761) ([e6a8dfa](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e6a8dfa))


### Features

* **exponea:** custom category per consent ([2b51448](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2b51448))
* **exponea:** exponea purchase, purchase line, product view, basket update, consent implementation ([665a485](https://gitlab.smartbase.sk/dev/django_smartshop/commit/665a485))
* **tracking:** implemented datalayer properties [#6893](http://redmine.smartbase.sk/issues/6893) ([8122376](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8122376))
* [#6737](http://redmine.smartbase.sk/issues/6737) added option to sort values of attribute option group ([359f972](https://gitlab.smartbase.sk/dev/django_smartshop/commit/359f972))
* [#6737](http://redmine.smartbase.sk/issues/6737) range filter ([3df48a7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3df48a7))
* elasticsearch index split by type, sort in buckets group by parent ([aaa4746](https://gitlab.smartbase.sk/dev/django_smartshop/commit/aaa4746))
* pagination in catalog ([a46f1c2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a46f1c2))
* recreate mapping + reindex ([15a95f6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/15a95f6))
* reindex to work with types ([24d413a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/24d413a))



<a name="0.2.7"></a>
## [0.2.7](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.6...0.2.7) (2019-03-29)


### Bug Fixes

* **build:** removed flower for throwing an error after celery build ([b528736](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b528736))


### Features

* [#6365](http://redmine.smartbase.sk/issues/6365) refactored elements to work with prerendered templates ([d23c2d3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d23c2d3))
* group attribute values in product detail elastic ([4a68ae5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4a68ae5))
* prerendering task to prerender pages from sitemap ([6ceebf4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6ceebf4))
* product detail group attributes rework with multiple options, search group by rework ([c4d4e86](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c4d4e86))
* **catalog:** remove by color agg, group by search attr aggregation ([ebe770d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ebe770d))
* rework group in list key generator ([d164237](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d164237))
* **account:** contact person for company in register and edit profile ([b59aac3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b59aac3))
* **catalog:** group by parent rework ([f50f1ce](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f50f1ce))
* **purchase:** [#6453](http://redmine.smartbase.sk/issues/6453) Loyalty program ([560064e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/560064e))


### Performance Improvements

* improved price incl_tax method perf ([bbbc5e4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bbbc5e4))



<a name="0.2.6"></a>
## [0.2.6](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.5...0.2.6) (2019-02)


### Bug Fixes

* **catalog:** variant in detail problem fix ([fb688ae](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fb688ae))


### Features

* **locale:** domain based locale ([d44866f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d44866f))
* [#6438](http://redmine.smartbase.sk/issues/6438) sitemap moved to disk ([a66af86](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a66af86))
* **account:** password change ([da0a32a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/da0a32a))
* **catalog:** group by name in catalog filters ([6e5ddc3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6e5ddc3))
* **catalog:** group by name in filters, horizontal filter - hide empty filter blocks ([eee9c0c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/eee9c0c))
* **isklad:** initial implementation API ([6af7082](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6af7082))
* **pricing:** auto recalculation by currency ratio ([be72930](https://gitlab.smartbase.sk/dev/django_smartshop/commit/be72930))


### Performance Improvements

* **admin:** added autocomplete to category admin 'relative to' field ([be4fd35](https://gitlab.smartbase.sk/dev/django_smartshop/commit/be4fd35))
* **tqdm:** added tqdm mininterval ([2cb94f9](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2cb94f9))



<a name="0.2.5"></a>
## [0.2.5](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.4...0.2.5) (2019-02-01)


### Bug Fixes

* [#5681](http://redmine.smartbase.sk/issues/5681) es7 syntax moved into js ([e07bc2e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e07bc2e))
* [#5681](http://redmine.smartbase.sk/issues/5681) fix of misundersood literal ([cffb34b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/cffb34b))
* [#5681](http://redmine.smartbase.sk/issues/5681) fixed unsupported syntax for ie in catalog filter ([a0a647a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a0a647a))
* [#5681](http://redmine.smartbase.sk/issues/5681) old polyfill replaced with babel-polyfill ([7aa33a4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7aa33a4))
* [#5935](http://redmine.smartbase.sk/issues/5935) searching when include aggs disabled results in error ([28b69a3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/28b69a3))
* fixed long load of product admin by adding DAL filters ([b41e05e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b41e05e))
* **catalog:** fix feed errors in API ([8297212](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8297212))
* **catalog:** sort by sold count feature ([cf40039](https://gitlab.smartbase.sk/dev/django_smartshop/commit/cf40039))
* **https:** django checks secure connection in custom header ([504faf0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/504faf0))
* fixed NPE [#5964](http://redmine.smartbase.sk/issues/5964) ([83bde04](https://gitlab.smartbase.sk/dev/django_smartshop/commit/83bde04))
* maximal height of horizontal filter ([670efdd](https://gitlab.smartbase.sk/dev/django_smartshop/commit/670efdd))
* pip version fixed to 18.1 ([860058d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/860058d))


### Features

* [#3618](http://redmine.smartbase.sk/issues/3618) added gift per product feature ([e9fa543](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e9fa543))
* [#4511](http://redmine.smartbase.sk/issues/4511) delivery times definition admin ([07492d0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/07492d0))
* added EXTERNAL_WAREHOUSE_STOCK, END_OF_SALE stock states ([d0e805d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d0e805d))
* added overrideable 404 catalog handler for easy redirects ([dd7fc13](https://gitlab.smartbase.sk/dev/django_smartshop/commit/dd7fc13))
* **catalog:** improve aogv query with materialized view ([b1deedb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b1deedb))
* **consent:** dynamic consents implementation, custom show in process/user profile ([dc1b015](https://gitlab.smartbase.sk/dev/django_smartshop/commit/dc1b015))
* **delivery:** added shop store pickup delivery service type [#5766](http://redmine.smartbase.sk/issues/5766) ([bd0a720](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bd0a720))
* **price:** old price feature in catalog + detail (elastic) ([37a8b30](https://gitlab.smartbase.sk/dev/django_smartshop/commit/37a8b30))
* preselect country based on selected currency [#5151](http://redmine.smartbase.sk/issues/5151) ([d7e3fe6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d7e3fe6))



<a name="0.2.4"></a>
## [0.2.4](https://gitlab.smartbase.sk/dev/django_smartshop/compare/0.2.3...0.2.4) (2019-01-03)


### Bug Fixes

* fixed big with non-root cms page breaking category display ([794b094](https://gitlab.smartbase.sk/dev/django_smartshop/commit/794b094))


### Features

* **catalog:** [#3126](http://redmine.smartbase.sk/issues/3126) Catalog filter structure improvement ([d6e27f0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d6e27f0))
* **catalog:** rework aggregations ([6605537](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6605537))
* added flower ([09ecc1e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/09ecc1e))


### Performance Improvements

* removed fetch for all categories ([1dc4714](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1dc4714))



<a name="0.2.3"></a>
## [0.2.3](http:///Workspace/__GitLab/django_smartshop/compare/0.2.2...0.2.3) (2018-12-04)


### Bug Fixes

* [#4847](http:///Workspace/__GitLab/django_smartshop/issues/4847) fixed dashboard statistics in admin ([6b73262](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6b73262))
* fix_migrations now skip empty migration folders on core apps ([939a76c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/939a76c))
* fixed merge_basket functionality for configured lines ([1c82cbe](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1c82cbe))


### Features

* add cachalot ([606ccb5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/606ccb5))
* added chain reload of uwsgi to fast deploy ([a1e72be](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a1e72be))
* added fast production build script ([736725d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/736725d))
* added previous dataseries to dashboard graph ([8330c68](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8330c68))
* fast deploy production script ([984d5c0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/984d5c0))



<a name="0.2.2"></a>
## [0.2.2](http:///Workspace/__GitLab/django_smartshop/compare/0.2.1...0.2.2) (2018-11-08)


### Bug Fixes

* security fix of chart urls ([2f3afe3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2f3afe3))
* translated statemachine filters in admin ([3257d9e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3257d9e))


### Features

* [#4511](http:///Workspace/__GitLab/django_smartshop/issues/4511) enable custom holidays date range definition ([de0419f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/de0419f))
* add total sum to purchase admin view ([a965064](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a965064))
* merge core json package with additional from project ([bce18d8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bce18d8))



<a name="0.2.1"></a>
## [0.2.1](http:///Workspace/__GitLab/django_smartshop/compare/0.2.0...0.2.1) (2018-10-01)


### Bug Fixes

* **database:** fixed race condition on invoice and purchase number generation ([d4389d3](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d4389d3))
* **invoice:** [#4779](http:///Workspace/__GitLab/django_smartshop/issues/4779) unification of variable symbol in all files ([76150b1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/76150b1))
* **oauth:** google, fb oauth urls ([f892456](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f892456))
* **purchase:** lock purchase table in purchase create ([398fb36](https://gitlab.smartbase.sk/dev/django_smartshop/commit/398fb36))
* **purchase_process:** lock basket, purchase process in purchase finalization ([4685a38](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4685a38))


### Features

* allow overriding of minimal amount for free shipping ([710dc9f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/710dc9f))
* sentry logging enabled ([bf9bdeb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bf9bdeb))
* **catalog:** [#4960](http:///Workspace/__GitLab/django_smartshop/issues/4960) added disable copy functionality to product detail ([afcac1b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/afcac1b))
* **health_check:** health check for db, cache, storage, celery, disk, rabbitmq, elastic, mail ([7b30ab5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7b30ab5))
* **heureka:** heureka for CZ ([f8b457c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f8b457c))
* **logging:** log errors messages from noreply@smartbase.sk ([7e68809](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7e68809))
* **multi_site:** allow setting default currency for site alias ([53e81ca](https://gitlab.smartbase.sk/dev/django_smartshop/commit/53e81ca))
* **multisite:** [#4802](http:///Workspace/__GitLab/django_smartshop/issues/4802) multisite emails implementation ([5c586fd](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5c586fd))



<a name="0.2.0"></a>
## [0.2.0](http:///Workspace/__GitLab/django_smartshop/compare/0.1.0...0.2.0) (2018-09-03)


### Bug Fixes

* **account:** changed way of creating and checking temp order url ([ba3a870](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ba3a870))
* **blog:** feed blogs in elastic with translations ([e02ac1e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e02ac1e))
* **catalog:** add missing translations for various models in core ([8b72318](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8b72318))
* **catalog:** fixed bad url for price ([68f14b7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/68f14b7))
* **catalog:** fixed catalog search widget, added full_name property to full_path on save ([6c5293f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6c5293f))
* **catalog:** fixed removing category when removeAll filters is pressed [#2756](http:///Workspace/__GitLab/django_smartshop/issues/2756) ([aeb973d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/aeb973d))
* **catalog:** fixed translation of and separator for manufacturers and categories ([773b272](https://gitlab.smartbase.sk/dev/django_smartshop/commit/773b272))
* **common:** changed redis cache get_or_set method ([9e25413](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9e25413))
* **dpd:** parcels (labels) for DPD are created separately for every quantity ([82c5077](https://gitlab.smartbase.sk/dev/django_smartshop/commit/82c5077))
* **elastic:** removed filters from category count ([5c52de5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5c52de5))
* **fonts:** rename wrong font files ([d7b919c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d7b919c))
* **gopay:** production mode - add to config constance ([1015e1d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1015e1d))
* **invoice:** fixed wrong invoice number generation [#2968](http:///Workspace/__GitLab/django_smartshop/issues/2968) ([8bbd65b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8bbd65b))
* **invoicing:** fixed numbering increment on invoices and credit notes + added tests ([3bb8850](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3bb8850))
* **locale:** locale from master ([0c4d156](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0c4d156))
* **macroproduct:** fixed wrong calculation of macroproduct price excl tax ([1aa6f38](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1aa6f38))
* **mailer:** fixed SellerCompany import ([06c9ce8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/06c9ce8))
* **paypal:** repay canceled PayPal payment [#4704](http:///Workspace/__GitLab/django_smartshop/issues/4704) ([3afde63](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3afde63))
* **pricing:** currency switching ([ace6d7d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ace6d7d))
* **process:** [#2660](http:///Workspace/__GitLab/django_smartshop/issues/2660) fixed wrong calculation of price excluding tax for services ([8430a85](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8430a85))
* **process:** fixed generating credit note even when no invoice existed ([cf0543c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/cf0543c))
* **process:** fixed not working errors on company data [#2897](http:///Workspace/__GitLab/django_smartshop/issues/2897) ([a0e908d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a0e908d))
* **product_configurator:** [#1480](http:///Workspace/__GitLab/django_smartshop/issues/1480) fixed add to purchase configuration, when doesn't exist ([d266f2d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d266f2d))
* **product_configurator:** cleanup code, added configs to invoices ([5f0c034](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5f0c034))
* **purchase:** [#2391](http:///Workspace/__GitLab/django_smartshop/issues/2391) fixed canceling delivery after canceling payment error, canceling delivery now doesn't affect payment ([94c4e15](https://gitlab.smartbase.sk/dev/django_smartshop/commit/94c4e15))
* **purchase:** first country is now pre-selected [#4265](http:///Workspace/__GitLab/django_smartshop/issues/4265) ([fad6f7c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fad6f7c))
* favicon for webniture removed ([11bce5e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/11bce5e))
* **purchase:** generate credit notes when cancelling purchase and invoice exists ([a829064](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a829064))
* **purchase:** get_products method fixed ([865b3f4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/865b3f4))
* **purchase:** process to cancel state fix, free reserved in cancel state fix ([7c4a114](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7c4a114))
* **purchase:** save purchase process in previous state if dpd raise error ([d1774b9](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d1774b9))
* **purchase:** show one-time order summary after purchase, working only for besteron before ([bf2d3c1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bf2d3c1))
* **purchase_process:** added missing app label ([537849b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/537849b))
* **SAEC:** improved mail textation to comply ([22b55b7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/22b55b7))
* **seo:** fixed language code ([dfaad02](https://gitlab.smartbase.sk/dev/django_smartshop/commit/dfaad02))
* **seo:** moved sitemap to seo package for better override ([8090254](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8090254))
* **wishlist:** [#3203](http:///Workspace/__GitLab/django_smartshop/issues/3203) fix sending notification mails ([a816336](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a816336))
* addToBasket properly read data from data attribute ([5901a3b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5901a3b))
* corrected loading of plugin templates ([e2eaabb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e2eaabb))
* fix for megamenu opening script ([2ddb4bc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2ddb4bc))
* fixed product tiles throwing exception ([13981d8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/13981d8))
* removed ES6 from non-builded GDPR script causing IE11 not-working ([6a7016c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6a7016c))
* replace datetime with timezones ([ff9e7fe](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ff9e7fe))
* update basket quantity moved to separate function to be called only on inner component changes ([3401351](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3401351))


### Code Refactoring

* **invoice:** reorganization and cleanup of invoice generations ([61b8e81](https://gitlab.smartbase.sk/dev/django_smartshop/commit/61b8e81))


### Features

* **admin:** added shop version information ([0b3f4aa](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0b3f4aa))
* **admin:** export of purchase invoicing info [#2636](http:///Workspace/__GitLab/django_smartshop/issues/2636) ([72a89f1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/72a89f1))
* **admin:** improved purchase admin [#3651](http:///Workspace/__GitLab/django_smartshop/issues/3651) ([0d0f26e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0d0f26e))
* **catalog:** [#4044](http:///Workspace/__GitLab/django_smartshop/issues/4044) multi site catalog definition implementation, elasticsearch rework ([ab594f6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ab594f6))
* **catalog:** added cache and iterative cache for catalog queries ([3537961](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3537961))
* **catalog:** added option to select main product for Macro ([b4212e0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b4212e0))
* **catalog:** category tile can combine manufacturer in link [#4227](http:///Workspace/__GitLab/django_smartshop/issues/4227) ([41504a6](https://gitlab.smartbase.sk/dev/django_smartshop/commit/41504a6))
* **catalog:** possibility to ignore attribute groups within creating product variants in product detail ([52daf85](https://gitlab.smartbase.sk/dev/django_smartshop/commit/52daf85))
* **catalog:** url contains category slug ([f194f1b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f194f1b))
* **cofidis:** [#4544](http:///Workspace/__GitLab/django_smartshop/issues/4544) cofidis loans payment ([00cac75](https://gitlab.smartbase.sk/dev/django_smartshop/commit/00cac75))
* **constance:** allow constance config for users ([d93e81b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d93e81b))
* **contact:** detail page for store [#4067](http:///Workspace/__GitLab/django_smartshop/issues/4067) ([c9e96eb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c9e96eb))
* **core:** activated commit lint ([69644bb](https://gitlab.smartbase.sk/dev/django_smartshop/commit/69644bb))
* **currency:** [#4147](http:///Workspace/__GitLab/django_smartshop/issues/4147) free shipping for currencies implementation ([a7ecd5d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a7ecd5d))
* **gpwebpay:** GPWebPay implementation ([23a6f86](https://gitlab.smartbase.sk/dev/django_smartshop/commit/23a6f86))
* **heureka:** added dpd_pickup to heureka feed based on package dimensions [#3546](http:///Workspace/__GitLab/django_smartshop/issues/3546) ([7c9e23f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7c9e23f))
* **integration:** [#4045](http:///Workspace/__GitLab/django_smartshop/issues/4045) migration of catalog and users from presta shop ([9c61b07](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9c61b07))
* **integration:** add pandoc package instalation as dependency for gopay payment gateway integration to gitlabci ([3b0cd03](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3b0cd03))
* **integration:** add pandoc package to vagrant as dependency for gopay payment gateway integration ([0e1af61](https://gitlab.smartbase.sk/dev/django_smartshop/commit/0e1af61))
* **integration:** added braintree integration ([ab129be](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ab129be))
* **invoice:** generating of partial credit notes [#3730](http:///Workspace/__GitLab/django_smartshop/issues/3730) ([c587f2b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c587f2b))
* **invoice:** show next invoicing number in admin ([8f26663](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8f26663))
* **invoicing:** added delivery and due date fields for more control ([f6f572e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f6f572e))
* **invoicing templates:** [#2623](http:///Workspace/__GitLab/django_smartshop/issues/2623) - consolidation of invoicing templates ([de4b521](https://gitlab.smartbase.sk/dev/django_smartshop/commit/de4b521))
* **invoicing templates:** [#2623](http:///Workspace/__GitLab/django_smartshop/issues/2623) - consolidation of invoicing templates ([71dd25d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/71dd25d))
* **invoicing templates:** [#2623](http:///Workspace/__GitLab/django_smartshop/issues/2623) - consolidation of invoicing templates ([87f5b17](https://gitlab.smartbase.sk/dev/django_smartshop/commit/87f5b17))
* **logging:** added LogEntry history to admin ([1822f57](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1822f57))
* **mailer:** added mails for created order ([ce3a097](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ce3a097))
* **multisite:** [#4414](http:///Workspace/__GitLab/django_smartshop/issues/4414) Purchase, User and Basket - relation with Site ([d6a164f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d6a164f))
* **multisite:** tracker of income from subshops [#4055](http:///Workspace/__GitLab/django_smartshop/issues/4055) ([54995a0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/54995a0))
* [#3652](http:///Workspace/__GitLab/django_smartshop/issues/3652) create competition app ([fc9298d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/fc9298d))
* [#3924](http:///Workspace/__GitLab/django_smartshop/issues/3924) added support for subscriptions in braintree ([93b863d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/93b863d))
* [#4044](http:///Workspace/__GitLab/django_smartshop/issues/4044) added muli_site app ([83a302f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/83a302f))
* [#4048](http:///Workspace/__GitLab/django_smartshop/issues/4048) added querybuilder app ([65ba6e5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/65ba6e5))
* [#4052](http:///Workspace/__GitLab/django_smartshop/issues/4052) finished ucto integration ([e0f8b1b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e0f8b1b))
* [#4052](http:///Workspace/__GitLab/django_smartshop/issues/4052) ucto integration work in progress ([3c5a92e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3c5a92e))
* [#4052](http:///Workspace/__GitLab/django_smartshop/issues/4052) ucto integration work in progress ([c0a0d3d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c0a0d3d))
* [#4052](http:///Workspace/__GitLab/django_smartshop/issues/4052) ucto integration work in progress ([9f3516d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9f3516d))
* [#4199](http:///Workspace/__GitLab/django_smartshop/issues/4199) paypal finalization, error handling ([2f59916](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2f59916))
* [#4199](http:///Workspace/__GitLab/django_smartshop/issues/4199) PayPal integration ([1f365c8](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1f365c8))
* [#4199](http:///Workspace/__GitLab/django_smartshop/issues/4199) use payment detail in API ([d2c21db](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d2c21db))
* [#4471](http:///Workspace/__GitLab/django_smartshop/issues/4471) added plugin for lists with icons for generic pages ([4a9c023](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4a9c023))
* [#4539](http:///Workspace/__GitLab/django_smartshop/issues/4539) command for downlaoding psc data and started work on autocomplete ([d3da44f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/d3da44f))
* [#4539](http:///Workspace/__GitLab/django_smartshop/issues/4539) finished psc autocomplete ([b8d3913](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b8d3913))
* [#4539](http:///Workspace/__GitLab/django_smartshop/issues/4539) moved psc autocomplete to new app ([cfb14d0](https://gitlab.smartbase.sk/dev/django_smartshop/commit/cfb14d0))
* added actions to product admin to be able to move multiple product to category or collection ([e1704e2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e1704e2))
* added color variant rgb selection option ([7904c80](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7904c80))
* **seo:** heureka view loads asynchronously ([19cf163](https://gitlab.smartbase.sk/dev/django_smartshop/commit/19cf163))
* added djangocms-icon model for plugins ([1477558](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1477558))
* **payment:** [#4543](http:///Workspace/__GitLab/django_smartshop/issues/4543) add pay (again) button to purchase detail ([abdda5c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/abdda5c))
* **plugin:** added django_unused_media ([e29791c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/e29791c))
* **plugin:** new store locator, store slider ([b8295e5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b8295e5))
* **plugins:** added storytelling plugin ([2af8aa7](https://gitlab.smartbase.sk/dev/django_smartshop/commit/2af8aa7))
* **process:** throw readable error when the state is not runnable ([6432c0c](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6432c0c))
* **purchase:** [#2886](http:///Workspace/__GitLab/django_smartshop/issues/2886) prefill country if it is only one available ([6f2e03f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6f2e03f))
* **purchase:** validate if user agrees with longer delivery [#1707](http:///Workspace/__GitLab/django_smartshop/issues/1707) ([a73cedc](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a73cedc))
* **purchase_process:** [#3212](http:///Workspace/__GitLab/django_smartshop/issues/3212) Visualize purchase process ([a3b891d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a3b891d))
* **search:** added button to admin to feed elastic search ([c2fc29d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c2fc29d))
* **security:** implementation pgcrypto fields, secured media ([c9da827](https://gitlab.smartbase.sk/dev/django_smartshop/commit/c9da827))
* **seo:** added adwords feed ([5b649ea](https://gitlab.smartbase.sk/dev/django_smartshop/commit/5b649ea))
* **seo:** sitemap asynchronous caching ([b0f3898](https://gitlab.smartbase.sk/dev/django_smartshop/commit/b0f3898))
* **server:** added pagespeed nginx plugin, improves pagesped score ([573fa71](https://gitlab.smartbase.sk/dev/django_smartshop/commit/573fa71))
* **service:** added api connector id for integrations ([3f792e5](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3f792e5))
* **style:** removed DjangoCMS logo ([9bcf324](https://gitlab.smartbase.sk/dev/django_smartshop/commit/9bcf324))
* **warehouse:** extended warehouse support ([a79d52d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a79d52d))
* added ES function score to be able boost filtered subset and added field boosts to dynamic pref ([a7e2967](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a7e2967))
* added fix_migrations for fixing migrations after override ([ce9b1aa](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ce9b1aa))
* added generice importer ([4d6dd07](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4d6dd07))
* added new contact form plugin ([1702a97](https://gitlab.smartbase.sk/dev/django_smartshop/commit/1702a97))
* added new set of sass mixins ([7f465e4](https://gitlab.smartbase.sk/dev/django_smartshop/commit/7f465e4))
* added option to exclude aggregation from catalog api ([ab10a7e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ab10a7e))
* added option to product END OF SALE ([002a60e](https://gitlab.smartbase.sk/dev/django_smartshop/commit/002a60e))
* added template loader caching ([a87985d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/a87985d))
* automatization of purchases to mark them as paid if email from DPD was received ([3be5974](https://gitlab.smartbase.sk/dev/django_smartshop/commit/3be5974))
* django version upgrade to 1.11.15 [#4590](http:///Workspace/__GitLab/django_smartshop/issues/4590) add attachment, Old Price, importer update ([02a5e02](https://gitlab.smartbase.sk/dev/django_smartshop/commit/02a5e02))
* support view ([6195bd1](https://gitlab.smartbase.sk/dev/django_smartshop/commit/6195bd1))
* support view ([190f386](https://gitlab.smartbase.sk/dev/django_smartshop/commit/190f386))
* **warehouse:** new document types (incoming outgoing) ([ae2657d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/ae2657d))
* **warehouse:** new document types (incoming, outgoing) ([945140f](https://gitlab.smartbase.sk/dev/django_smartshop/commit/945140f))
* **warehouse:** splitting invoices for multiple warehouses ([345643d](https://gitlab.smartbase.sk/dev/django_smartshop/commit/345643d))
* **warehouse:** splitting orders based on warehouse and producer [#3703](http:///Workspace/__GitLab/django_smartshop/issues/3703) ([8f17a9b](https://gitlab.smartbase.sk/dev/django_smartshop/commit/8f17a9b))
* **wishlist:** added watchdog for price ([4fc598a](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4fc598a))


### Performance Improvements

* **catalog:** common methods from different item moved to mixin and removed unused methods ([4e51161](https://gitlab.smartbase.sk/dev/django_smartshop/commit/4e51161))
* **elastic:** improved feed speed, fixed translations ([f848be2](https://gitlab.smartbase.sk/dev/django_smartshop/commit/f848be2))
* log only ERROR to console in production ([bd26f19](https://gitlab.smartbase.sk/dev/django_smartshop/commit/bd26f19))


### BREAKING CHANGES

* **invoice:** Old invoices will become unreachable after this update because of change to generic relation
* **catalog:** This change is not backward compatible and it is
necessary to migrate data from old version and also changed overridden
models in project. This change will REMOVE any data in changed fields.



