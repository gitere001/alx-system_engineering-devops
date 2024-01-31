# 0x06. Regular expression
## This directory contain files for learning purpose about Regular expression
For this project, I build  regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a

Resources
https://intranet.alxswe.com/rltoken/6VeaVMaugIxcFAwA27TBdQ
https://intranet.alxswe.com/rltoken/rntjh3-3S86zt0Qy28L10w
https://intranet.alxswe.com/rltoken/RGkVuw1lZ_hoCCbLsiOAhg
https://intranet.alxswe.com/rltoken/Vwm8lpMUGa4x_FBtlyUQ8g
https://intranet.alxswe.com/rltoken/XsQ6rzS1uy-E6bnswUqIKg