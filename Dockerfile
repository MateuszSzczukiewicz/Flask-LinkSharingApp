FROM --platform=$BUILDPLATFORM python:3.13-alpine AS builder

WORKDIR /app

COPY requirements.txt /app

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000
ENV FLASK_APP=link_sharing_app

ENTRYPOINT ["python3"]
CMD ["-m", "flask", "--app", "link_sharing_app", "run"]

FROM builder as dev-envs

RUN apk update && apk add git

RUN addgroup -S docker && adduser -S --shell /bin/bash --ingroup docker

COPY --from=gloursdocker/docker / /
