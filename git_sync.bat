@echo off
echo GitHub와 동기화 중...
git add .
git commit -m "자동 동기화: %date% %time%"
git push origin main
echo 완료.
pause
