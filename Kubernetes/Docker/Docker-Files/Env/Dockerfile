FROM almalinux
RUN echo "Peddireddy Hari Vardhan Reddy"
EXPOSE 80/tcp
LABEL Name="Hari"\
      Year=2023 \
      Course="DevOps"\
      Hours="150HRS"
ENV name=peddireddy\
    Year=2023 \
    Course=DevOps\
    Hours=150
RUN yum install nginx -y
CMD [ "nginx" ,"-g" ,"daemon off ;"]