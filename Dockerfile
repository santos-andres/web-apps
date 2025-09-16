FROM python:3.13

# Expose port you want your app on
WORKDIR /app

#should be always expose this port?
EXPOSE 5050
#and this?
#EXPOSE 8501

# Upgrade pip and install requirements
# 
COPY requirements.txt .
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt
#RUN apt-get update
#RUN apt-get install -y unixodbc

#RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -


#Download appropriate package for the OS version
#Choose only ONE of the following, corresponding to your OS version
#Debian 11
#RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
#RUN apt-get update
#RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
# optional: for bcp and sqlcmd
#RUN ACCEPT_EULA=Y apt-get install -y mssql-tools18
#RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
#RUN . ~/.bashrc
# optional: for unixODBC development headers
#RUN apt-get install -y unixodbc-dev
# optional: kerberos library for debian-slim distributions
#RUN apt-get install -y libgssapi-krb5-2


# Copy app code and set working directory
#COPY . .
COPY src/app.py /app/app.py
# Run
#ENTRYPOINT ["python3", "app.py"]
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=5050", "--server.address=0.0.0.0"]
