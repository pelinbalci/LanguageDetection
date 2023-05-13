This project is prepared by this github page:
https://github.com/AssemblyAI-Examples/ml-fastapi-docker-heroku

Here is the YouTube link:
https://www.youtube.com/watch?v=h5wLuVDr0oc

Other references for FASTAPI:
- https://www.kaggle.com/datasets/basilb2s/language-detection?resource=download
- https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package
- https://stackoverflow.com/questions/5834014/lf-will-be-replaced-by-crlf-in-git-what-is-that-and-is-it-important

## Build Docker

Open terminal:

docker build -t language-detection-app .

docker run -p 80:80 language-detection-app 

After that you can reach the page from: http://localhost:80

Hopefully you will se:
{"health_check":"OK","model_version":"0.1.0"}

If you want to try the model just type: 
http://localhost:80/docs

Do not close the docker. 

Now if you want to see your streamlit app is working, open another terminal:

streamlit run streamlit_app.py







