@echo off

for /f "delims=" %%a in ('dir /b/a-d/oN *.*') do echo %%a >>saveFileName.txt