@echo off
if "%1" == "" goto NOVER
mkdir lib\Win\x86
mkdir lib\Win\x64

cd ..\api

if "%ProgramFiles(x86)%" == "" goto L1
call "%ProgramFiles(x86)%\Microsoft Visual Studio 9.0\VC\vcvarsall.bat"
set MAKENSIS="%ProgramFiles(x86)%\NSIS\makensis.exe"
goto L2
:L1
call "%ProgramFiles%\Microsoft Visual Studio 9.0\VC\vcvarsall.bat"
set MAKENSIS="%ProgramFiles%\NSIS\makensis.exe"
:L2
devenv indigo-api.sln /build "ReleaseJNI|x64"
devenv indigo-api.sln /build "ReleaseJNI|Win32"

cd java
call compile.bat
cd ..\renderer\java
call compile.bat
cd ..\..\..\legio

copy ..\api\java\dist\indigo-java.jar lib\
copy ..\api\renderer\java\dist\indigo-renderer-java.jar lib\
cd src
javac -cp ..\lib\indigo-java.jar;..\lib\indigo-renderer-java.jar com/gga/indigo/legio/*.java
jar cvfm ..\legio.jar ..\manifest.mf com/gga/indigo/legio/*.class
cd ..

call dll-copy.bat
echo start javaw -jar -Xss10m legio.jar > launch.bat

%MAKENSIS% /DVERSION=%1 legio_installer.nsi 
goto END

:NOVER
echo Specify version please
:END
