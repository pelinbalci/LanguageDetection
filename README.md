# FAST API

https://github.com/AssemblyAI-Examples/ml-fastapi-docker-heroku

https://www.youtube.com/watch?v=h5wLuVDr0oc

https://www.kaggle.com/datasets/basilb2s/language-detection?resource=download

https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package

https://stackoverflow.com/questions/5834014/lf-will-be-replaced-by-crlf-in-git-what-is-that-and-is-it-important

## Build Docker

docker build -t language-detection-app .

docker run -p 80:80 language-detection-app 

check: http://localhost:80

{"health_check":"OK","model_version":"0.1.0"}

http://localhost:80/docs





