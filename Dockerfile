FROM fedora:35
COPY --from=docker.io/minio/mc:latest /usr/bin/mc /usr/bin/mc
RUN yum -y install fio python3-six
ENTRYPOINT ["/usr/bin/fio"]
