# Use a lightweight base image
FROM alpine:latest

# Add a simple message
RUN echo "Hello from Docker!" > /hello.txt

# Set the default command
CMD ["cat", "/hello.txt"]
