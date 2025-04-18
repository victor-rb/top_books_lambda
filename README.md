# 📚 Web Crawler Lambda (Python)

This project is an **AWS Lambda function** written in **Python** that crawls a given webpage and extracts specific information:  
**Book Name**, **Author**, and **Year of Publication**.

It runs inside a **Docker container**, making it easy to test locally and deploy to AWS.

---

## 🚀 Features

- 🌐 Crawls a target webpage
- 🧠 Extracts:
  - Title / Name
  - Author
  - Year of publication
- 📦 Packaged as a Lambda-ready Docker image

---

## 🛠 Tech Stack

- Python 3.10
- BeautifulSoup / Requests (for web scraping)
- AWS Lambda (container-based)
- Docker

## 🧪 Run Locally (via Docker)

```
docker build -t lambda-docker-python .

docker run -d -p 9000:8080 --name lambda-top-books lambda-docker-python

```


