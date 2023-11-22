FROM eclipse-temurin:17.0.8_7-jdk-jammy

# STEP 1: Add the helloworld directory in container, set working directory and make script executable
COPY . /opt
WORKDIR /opt
RUN chmod +x entry.sh

# STEP 2: Run the script that builds/starts the project
ENTRYPOINT ["/bin/sh","./entry.sh"]