FROM python:3.10.1

# Configure Poetry
ENV POETRY_VERSION=1.3.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

ENV QUOTES='/root/quotes'

# API KEYS
ENV BINANCEAPIKEY='bBs0XgyUMuVVAZYsjGR6batj6eQpxCpCUEdyR4UStXKDdJr6zkl0inKgWyiqAi11'
ENV BINANCEAPISECRET='7MbWaWly7AcKNTxFEb4OPLdKfDf0hzyhzK30Tz2D1Ly7eTIio6HcKzDBJBIDOnLT'

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app

RUN apt-get update && apt-get install tree
# install rclone
# RUN curl https://rclone.org/install.sh | bash
# RUN rclone --version
# COPY rclone /root/.config/rclone
# RUN ls /root/.config/rclone

# RUN rclone config file
# RUN rclone copy mega:/quotes/test quotes/test
# RUN tree .
# RUN pwd

RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/linux64/chrome-linux64.zip && unzip chrome-linux64.zip
RUN ls

# # Install dependencies
# COPY poetry.lock pyproject.toml ./
# RUN poetry install

# COPY . /app

# # run tests
# RUN poetry run pytest --disable-warnings
# # Run your app
# # CMD [ "poetry", "run", "python", "-c", "print('Hello, World!')" ]

