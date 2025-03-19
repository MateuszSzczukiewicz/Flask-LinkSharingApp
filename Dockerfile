FROM python:3.13-alpine AS builder

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir build

RUN python -m build --wheel

FROM python:3.13-alpine AS runner

WORKDIR /app

COPY --from=builder /app/dist/*.whl ./

RUN pip install --no-cache-dir *.whl waitress

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

EXPOSE 8000

COPY scripts/buildprod.sh /app
RUN chmod +x /app/scripts/buildprod.sh

ENTRYPOINT ["/app/scripts/buildprod.sh"]
