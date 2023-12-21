FROM almalinux

RUN echo "Peddireddy Hari Vardhan Reddy"
EXPOSE 80/tcp
RUN yum install nginx -y
RUN yum install mysql -y

CMD [ "nginx" ,"-g", "daemon off ;"]