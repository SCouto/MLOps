FROM jupyter/scipy-notebook:latest

WORKDIR /home/jovyan/work

EXPOSE 8888

RUN pip install pandas matplotlib scikit-learn

CMD ["start-notebook.sh", "--NotebookApp.token=''"]

