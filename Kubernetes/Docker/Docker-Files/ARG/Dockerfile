ARG version
FROM nginx:${version}
ARG Name
ARG Course
ENV Course=${Course}
ENV Name=${Name}
RUN echo "Course id ${Course}, and My Name is: ${Name}"
CMD [ "nginx", "-d", "daemon off ;"]
ENTRYPOINT [ "nginx" ,"-g", "daemon off ;" ]