@echo off
@echo.
@echo Videos can be created at various resolutions and framerates (FPS):
@echo.
@echo 1:  854x480  15FPS (low)
@echo 2: 1280x720  30FPS (medium)
@echo 3: 1920x1080 60FPS (high)
@echo 4: 2560x1440 60FPS (2k)
@echo 5: 3840x2160 60FPS (4k)
@echo.
choice /c 12345 /m "Select quality (1 to 5) or ^C to cancel..." /n

if errorlevel 5 goto K
if errorlevel 4 goto P
if errorlevel 3 goto H
if errorlevel 2 goto M
if errorlevel 1 goto L
goto end

:K
set folder=2160p60
set quality=k
goto exec
:P
set folder=1440p60
set quality=p
goto exec
:H
set folder=1080p60
set quality=h
goto exec
:M
set folder=720p30
set quality=m
goto exec
:L
set folder=480p15
set quality=l
goto exec

:exec
echo for %%p in (*.py) do manim %%p -q%quality%



dir *.mp4 /b/s | find /v "partial_movie_files" | find "%folder%" > %folder%.txt
ffmpeg

:end
