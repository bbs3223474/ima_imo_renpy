@echo off

title 递归转换文件

echo 开始转换！
echo.
for /R %%s in (*.txt) do (
	cscript //Nologo buriko2rpy.wsf "%%s"
	echo.
)
echo 转换结束！
echo.
pause