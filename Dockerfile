# Choose a python version that you know works with your application
FROM ghcr.io/astral-sh/uv:debian-slim

WORKDIR /app

# Copy requirements file
COPY --link pyproject.toml .

# Install the requirements using uv
RUN uv sync

# Copy application files
COPY --link causal_graphs.py .
COPY --link parser.py .



EXPOSE 8080

CMD [ "uv", "run", "marimo", "run", "causal_graphs.py", "--host", "0.0.0.0", "-p", "8080" ]
