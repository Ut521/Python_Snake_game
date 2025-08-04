FROM python:3.9

# Install dependencies for GUI and Pygame
RUN apt-get update && \
    apt-get install -y python3-dev python3-pip python3-tk libx11-dev libgl1-mesa-glx x11-xserver-utils && \
    pip install pygame

# Set work directory
WORKDIR /app

# Copy game files
COPY . .

# Set display env (for headless systems)
ENV DISPLAY=:0

# Run the game
CMD ["python3", "SnakeGame.py"]

