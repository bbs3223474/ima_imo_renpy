@echo off

title �ݹ�ת���ļ�

echo ��ʼת����
echo.
for /R %%s in (*.txt) do (
	cscript //Nologo buriko2rpy.wsf "%%s"
	echo.
)
echo ת��������
echo.
pause