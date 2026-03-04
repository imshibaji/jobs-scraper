# Jobs Scraper

## Requirements

```bash
pip install -r requirements.txt
```

## Usage

```bash
python scraper.py
```

## Docker

```bash
docker build -t scraper .
docker run -p 8000:8000 scraper
```

## Docker Compose

```bash
docker compose up --build
```

## Deployment

```bash
docker pull imshibaji/jobs-scraper
docker run -p 8000:8000 imshibaji/jobs-scraper
```

## Docker Hub

You can find the Docker Hub image at [imshibaji/jobs-scraper](https://hub.docker.com/r/imshibaji/jobs-scraper).

## Stay in touch

If you have any questions or feedback about this project. Please reach out to me on [Twitter](https://twitter.com/shibaji_debnath) or [GitHub](https://github.com/imshibaji).

## License

[MIT License](https://github.com/imshibaji/jobs-api-server/blob/main/LICENSE)
