@echo off
REM Delete the build directory if it exists
if exist .\build (
    rmdir /s /q .\build
)

REM Run sphinx-build to generate documentation
sphinx-build docs\source .\build