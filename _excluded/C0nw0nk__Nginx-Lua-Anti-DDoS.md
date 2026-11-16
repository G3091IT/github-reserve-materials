> 【审计剔除 · 2026-11-11】初版闸门因泛化英文词（engineer/cms/archive）误收，经人工核对与「工程资料管理」主题无关，移入 _excluded 留痕。原路径 05_工程资料管理/C0nw0nk__Nginx-Lua-Anti-DDoS.md。

# C0nw0nk/Nginx-Lua-Anti-DDoS

- **仓库名**：C0nw0nk/Nginx-Lua-Anti-DDoS
- **原文链接**：https://github.com/C0nw0nk/Nginx-Lua-Anti-DDoS
- **Star 数**：1674（取自 GitHub 搜索 API；本环境数值可能偏高，待核实）
- **最近更新时间**：2026-10-16T17:39:59Z
- **许可证**：MIT
- **语言**：Lua
- **质量分 / 适配分 / 混合分**：94.2 / 12.0 / 57.2
- **结论**：ADOPT
- **标记**：无
- **领域适配**：领域词:engineer/cms/archive

## 用途摘要
A Anti-DDoS script to protect Nginx web servers using Lua with a HTML Javascript based authentication puzzle inspired by Cloudflare I am under attack mode an Anti-DDoS authentication page protect yourself from every attack type All Layer 7 Attacks Mitigating Historic Attacks DoS DoS Implications DDoS All Brute Force Attacks Zero day exploits Social Engineering Rainbow Tables Password Cracking Tools Password Lists Dictionary Attacks Time Delay Any Hosting Provider Any CMS or Custom Website Unlimited Attempt Frequency Search Attacks HTTP Basic Authentication HTTP Digest Authentication HTML Form Based Authentication Mask Attacks Rule-Based Search Attacks Combinator Attacks Botnet Attacks Unauthorized IPs IP Whitelisting Bruter THC Hydra John the Ripper Brutus Ophcrack unauthorized logins Injection Broken Authentication and Session Management Sensitive Data Exposure XML External Entities (XXE) Broken Access Control Security Misconfiguration Cross-Site Scripting (XSS) Insecure Deserialization Using Components with Known Vulnerabilities Insufficient Logging & Monitoring Drupal WordPress Joomla Flash Magento PHP Plone WHMCS Atlassian Products malicious traffic Adult video script avs KVS Kernel Video Sharing Clip Bucket Tube sites Content Management Systems Social networks scripts backends proxy proxies PHP Python Porn sites xxx adult gaming networks servers sites forums vbulletin phpbb mybb smf simple machines forum xenforo web hosting video streaming buffering ldap upstream downstream download upload rtmp vod video over dl hls dash hds mss livestream drm mp4 mp3 swf css js html php python sex m3u zip rar archive compressed mitigation code source sourcecode chan 4chan 4chan.org 8chan.net 8ch 8ch.net infinite chan 8kun 8kun.net anonymous anon tor services .onion torproject.org nginx.org nginx.com openresty.org darknet dark net deepweb deep web darkweb dark web mirror vpn reddit reddit.com adobe flash hackthissite.org dreamhack hack hacked hacking hacker hackers hackerz hackz hacks code coding script scripting scripter source leaks leaked leaking cve vulnerability great firewall china america japan russia .gov government http1 http2 http3 quic q3 litespeedtech litespeed apache torrents torrent torrenting webtorrent bittorrent bitorrent bit-torrent cyberlocker cyberlockers cyber locker cyberbunker warez keygen key generator free irc internet relay chat peer-to-peer p2p cryptocurrency crypto bitcoin miner browser xmr monero coinhive coin hive coin-hive litecoin ethereum cpu cycles popads pop-ads advert advertisement networks banner ads protect ovh blazingfast.io amazon steampowered valve store.steampowered.com steamcommunity thepiratebay lulzsec antisec xhamster pornhub porn.com pornhub.com xhamster.com xvideos xvdideos.com xnxx xnxx.com popads popcash cpm ppc

## 适配理由
⚠ 未命中任何任务关键词，可能不相关

## README 要点
[![Languages](https://img.shields.io/github/languages/count/C0nw0nk/Nginx-Lua-Anti-DDoS) ![Top language](https://img.shields.io/github/languages/top/C0nw0nk/Nginx-Lua-Anti-DDoS) ![File size](https://img.shields.io/github/size/C0nw0nk/Nginx-Lua-Anti-DDoS/lua/anti_ddos_challenge.lua)](https://github.com/C0nw0nk/Nginx-Lua-Anti-DDoS/wiki/funding) [![Build and Publish RPM/DEB Packages](https://github.com/C0nw0nk/Nginx-Lua-Anti-DDoS/actions/workflows/build-publish.yml/badge.svg)](https://github.com/C0nw0nk/Nginx-Lua-Anti-DDoS/actions/workflows/build-publish.yml)

[![Cloudflare I am Under Attack Mode!](https://blog.cloudflare.com/content/images/im_under_attack_page.png.scaled500.png)](https://github.com/C0nw0nk/Nginx-Lua-Anti-DDoS/wiki/funding)

[Master Branch for Modern Nginx Lua Builds](https://github.com/C0nw0nk/Nginx-Lua-Anti-DDoS/tree/master) - [Old Outdated Nginx Lua Builds use this branch](https://github.com/C0nw0nk/Nginx-Lua-Anti-DDoS/tree/old-outdated-nginx-lua-builds)

# Nginx-Lua-Anti-DDoS
A Anti-DDoS script to protect Nginx web servers using Lua with a Javascript based authentication puzzle inspired by Cloudflare I am under attack mode I built my own Anti-DDoS authentication HTML page puzzle intergrating my Lua, Javascript, HTML and HTTP knowledge.

Mitigate a DDoS attack of any size using my free DDoS protection. Don't get ddos attacked!

If you're under attack and use my script during the attack, visitors will receive an interstitial page for about five seconds while I analyze the traffic to make sure it is a legitimate human visitor.

This can protect you from many different forms of DDoS works with both HTTP and HTTPS / SSL traffic.

No limit on attack size
Uptime guarantee

100% asynchronous nonblocking I/O

# Features :

These are some of the features I built into the script so far.

## Security

Limit IP requests / Flooding

Ability to use Remote servers for Anti-DDoS data/key storage

Ability to use redis cache server for anti-ddos protection

Ability to use memcached server for anti-ddos protection

Automatically turn on Under Attack mode if DDoS detected

I am Under Attack Mode (DDoS Authentication HTML Page)

IP Address Whitelist

IP Subnet Ranges Whitelist

IP Address Blacklist

IP Subnet Ranges Blacklist

User-Agent Whitelist

User-Agent Blacklist

Protected area / Restricted access field username / password box to restrict access to sites / paths.

Enable or disable logging of users who either fail or succeed solving the authentication puzzle. (Fail2Ban users can use this to ban bots AI tools and IP addresses from the log file)

Range header filtering Most download / Video streaming sites and services use range headers this allows you to filter and block slowhttp / slowloris attack types

Remote storage encryption to protect sensative data stored on redis memcached etc

Storage compression on stored data to save disk/storage space/memory compression options of LuaLZW, Brotli, Zstd, Zlib, GZip, Google Snappy

## WAF (Web Application Firewall)

IPv4 and IPv6 blocking and whitelisting including subnet ranges.

User-Agent blocking and whitelisting to block bad bots and exploits / scanners.

Ability to inspect POST Data / Fields and block malicious POST requests / exploits.

Ability to inspect URL for malicious content SQL/SQI Injections XSS attacks / exploits.

Ability to inspect query strings and arguements for malicious content / exploits.

Ability to inspect all Request Headers provided by the client connecting.

Ability to inspect cookies for exploits.

## Caching Speed and Performance

Webpage Caching Ability/Feature to Cache webpages and Bypass Cache based on cookies or URL's

Webpage Caching Ability/Feature to Cache only when Cookies or URL's exist

Webpage Caching Ability/Feature to Cache only if page size is Larger than or Smaller than a certain size

Query String Sorting

Query String Whitelist

Query String Removal (It is a blacklist but it will just drop / remove the argument from the URL not block the request)

Minification / Compression of files removing white space and nulled out code / lines JS JavaScript, CSS Stylesheets, HTML etc

Ability to use Redis as a cache storage soloution

Ability to use Memcached as a cache storage soloution

Ability to use lrucache as a cache storage soloution

Ability to use shared.DICT memory as a cache storage soloution

Ability to encrypt stored data to protect from hosting hacks and information stealing / snooping

Ability to compress stored data to save disk/storage space/memory compression methods include LZW (LUALZW) ZSTD Zstandard, Brotli, Zlib, GZip, Google Snappy to save petabytes in cached storage space and reduced costs.

## Support for Additional services

Supports Tor services .Tor

Supports Lokinet services .Loki

Supports Ethereum name services .ENS

Supports The invisible internet project .i2p

Supports Freenet

Supports IPFS inter planetary file system

Supports IPNS inter planetary name system

Supports SWARM network

Supports Radicale

Supports any port matches node or hidden service that nginx is protecting

Supports zeronet

## Customization of error pages responses and webpage outputs

Custom error page interception to replace with your own error pages

Hide Web application errors such as PHP errorrs MySQL errors it will intercept them and display a custom error page instead of showing visitors sensative information

Modify webpage outputs to replace contents on pages / files

# Information :

If you have any bugs issues or problems just post a Issue request.

https://github.com/C0nw0nk/Nginx-Lua-Anti-DDoS/issues

If you fork or make any changes to improve this or fix problems please do make a pull request for the community who also use this. 

https://github.com/C0nw0nk/Nginx-Lua-Anti-DDoS/pulls

## Be sure to use the latest Nginx+Lua builds and libraries to avoid any issues.

# Usage / Installation :

Edit settings inside `anti_ddos_challenge.lua` to cater for your own unique needs or improve my work. (
...（截断，原文见链接）

## 核心代码片段（来源：CHANGELOG）
```lua
Version: 7.0
Date: 2026-10-16
- Performance Improvements on functions.

Version: 6.9
Date: 2026-10-15
- Add missing checks on localized_global.encrypt_storage_types and localized_global.storage_compression_types that allow for these vars to be controlled via overrides from nginx config etc if needed.
- Performance improvements on systems than can run 64bit compared to 32bit.

Version: 6.8
Date: 2026-10-15
- Added Feature ability to encrypt/compress only Content-Cache items that way IP addresses/Flood trackers can be stored unencrypted/uncompressed now it is optional and can choose.
- Fixed a bug where i named config_store.anti_ddos_table - config_store.anti_ddos_data by accident.

Version: 6.7
Date: 2026-10-14
- Improve performance of config vars by caching them so Lua garbage collector does not get thrashed creating and destroying tables.

Version: 6.6
Date: 2026-10-09
- Pre compile WAF rules to be faster.

Version: 6.5
Date: 2026-10-08
- Make the 1million IP limit on the Ram Cache configurable so users can change it at any time if you increase your lua_shared_dict capacity you can also increase this.

Version: 6.4
Date: 2026-10-07
- Improvements on speed avoiding memory thrashing / leaks etc.
- Make user-agent blacklist / whitelist matching faster.

Version: 6.3
Date: 2026-10-06
- Various speed and performance improvements re-order functions use caching and memory more efficiently.

Version: 6.2
Date: 2026-10-03
- Use Lua built in base64 and improve JS scrambler speed

Version: 6.1
Date: 2026-10-02
- FFI is faster than most functions so we use FFI in place with C code to improve performance
- Do not use math.pow anywhere any more so removed and speed up other functions
- Improve cookie matching on content-cache

Version: 6.0
Date: 2026-09-30
- Performance Improvements on IPv4/IPv6 matching

Version: 5.9
Date: 2026-09-30
- Improve performance fast IP range/address lookups

Version: 5.8
Date: 2026-09-28
- Added Feature Merge IP lists
- Added Feature auto add server IP address to IP lists
- Added Feature Compressed storage min/max size

Version: 5.7
Date: 2026-09-26
- Allow both tables or functions in script overrides

Version: 5.6
Date: 2026-09-26
- Tables into functions to defer execution so that input vars and strings execute in order of when called.

Version: 5.5
Date: 2026-09-24
- Remove un-needed vars and Optimise functions for runtime improvements.

Version: 5.4
Date: 2026-09-23
- Cache localized functions for better performance
- ngx.escape_uri faster than my function

Version: 5.3
Date: 2026-09-22
- Improvements on WAF checks and internal header checks

Version: 5.2
Date: 2026-09-21
- Fixes for multiple headers of the same type that Lua creates into a table just use the latest / last value.

Version: 5.1
Date: 2026-09-21
- localized.ngx.now()-localized.ngx.req.start_time() is faster than localized.ngx_var.request_time
- Use cached functions on other header checks for better performance.

Version: 5.0
Date: 2026-09-20
- ngx.req.get_method() is faster than ngx.var.request_method

Version: 4.9
Date: 2026-09-19
- Improve Performance of functions.

Version: 4.8
Date: 2026-09-18
- Caching on strings and Improvements.

Version: 4.7
Date: 2026-09-16
- Added Feature option to use alternative encryption for javascript puzzle default is hmac sha1 - xor added
- Reorder functions for execution priority

Version: 4.6
Date: 2026-09-14
- Performance improvements by caching outputs

Version: 4.5
Date: 2026-09-13
- Added Feature ZSTD Facebook Zstandard Compression support for storage
- Added Feature Google Snappy Compression support for storage
- Added Feature Brotli Compression support for storage

Version: 4.4
Date: 2026-09-12
- Added Feature resty zip compression for storage
- Re-ordered storage so that compression takes place before encryption and in reverse decryption happens before decompression the result is encrypted storage items are smaller a huge win.

Version: 4.3
Date: 2026-09-11
- Added Feature LZW compression on stored da
...（截断，原文见链接）
```
