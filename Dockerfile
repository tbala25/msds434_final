FROM python:3.10

RUN mkdir /msds434_final
ADD . /msds434_final

workdir /msds434_final
EXPOSE 8501

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "streamlit_dash.py", "--server.port=8501", "--server.address=0.0.0.0"]

