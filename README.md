# My Portfolio Website

![GitHub last commit](https://img.shields.io/github/last-commit/TadeopCreator/portfolio-website)
![GitHub repo size](https://img.shields.io/github/repo-size/TadeopCreator/portfolio-website)

A Dockerized Django portfolio website to showcase my work, skills, and more.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
- [Using Docker Desktop](#using-docker-desktop)
- [Technologies Used](#technologies-used)
- [License](#license)

## About

This is my personal portfolio website built with Django and Dockerized for easy deployment. It's a platform where I can showcase my projects, provide information about myself, and demonstrate my skills and experiences.

## Features

- **Project Showcase:** Display your projects with descriptions and links.
- **About Me:** Share your background, education, and interests.
- **Resume:** Upload your resume/CV for visitors to download.
- **Contact Form:** Allow visitors to get in touch with you.
- **Dockerized:** The project is containerized using Docker for easy deployment.

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo-name
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - **On Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **On macOS and Linux:**

     ```bash
     source venv/bin/activate
     ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

7. Open your web browser and visit [http://localhost:8000/](http://localhost:8000/) to view your website locally.

## Using Docker Desktop

**Building the Docker Image**:

   ```bash
   docker build -t my-django-app .
   ```

   - `docker build`: This command is used to build a Docker image from a Dockerfile.
   - `-t my-django-app`: The `-t` flag specifies a tag for the image. In this case, the tag is named `my-django-app`. You can think of the tag as a name for your image.
   - `.`: The period at the end indicates that the Dockerfile is in the current directory.

   This command builds an image based on the instructions in your Dockerfile, which is typically used to define the environment and dependencies for your Django application.

**Running the Django App Container**:

   ```bash
   docker run -d --network portfolio-network -p 8000:8000 my-django-app
   ```

   - `docker run`: This command is used to run a Docker container from an image.
   - `-d`: The `-d` flag runs the container in detached mode, meaning it runs in the background.
   - `--network portfolio-network`: This flag specifies the network to connect the container to. It appears you have a custom network named `portfolio-network` for your containers to communicate with each other.
   - `-p 8000:8000`: The `-p` flag maps ports from the host to the container. In this case, it maps port 8000 on your host machine to port 8000 in the container, allowing you to access your Django application in a web browser.
   - `my-django-app`: This is the name of the Docker image to run, which should match the tag you used when building the image.

   This command starts a new container based on the image you built earlier, and it will run your Django application.

Remember to ensure that your Django application is correctly configured to use the network and ports specified in the `docker run` command. This includes database and other service connections if needed. Additionally, make sure your Dockerfile sets up your Django environment correctly.

## Technologies Used

- Django
- Docker
- HTML/CSS
- JavaScript
- PostgreSQL

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
