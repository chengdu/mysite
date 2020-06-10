Speare Debug Server v1.0
(c) http://sevenuc.com

This is the Lua debugger for Speare code editor:
http://sevenuc.com/en/Speare.html

Package source: 
http://sevenuc.com/download/debugger.tar.gz

Directory Structure:

debugger
|____5.1
| |____lua_514    # Lua interpreter version 5.1.4
| |____lua_515    # Lua interpreter version 5.1.5
| |____sds.so     # Speare debug server for Lua 5.1
| |____server.lua # Server script
| |____socket     
| | |____core.so  # luasocket for Lua 5.1
| |____socket.lua # lua socket module
|____5.2
| |____lua_524    # Lua interpreter version 5.2.4
| |____sds.so     # Speare debug server for Lua 5.2
| |____server.lua # Server script
| |____socket
| | |____core.so  # luasocket for Lua 5.2
| |____socket.lua # lua socket module
|____5.3
| |____lua_535    # Lua interpreter version 5.3.5
| |____sds.so     # Speare debug server for Lua 5.3
| |____server.lua # Server script
| |____socket
| | |____core.so  # luasocket for Lua 5.3
| |____socket.lua # lua socket module
|____killlua.sh   # shell script to kill Lua process
|____README.txt   # readme for this package

Start Server:
$ ./lua_514 server.lua

You can directly replace the Lua interpreter under the
debugger directory with your customised version.

11/JUL/2019



