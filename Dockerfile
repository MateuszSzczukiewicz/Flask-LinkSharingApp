FROM python:3.13-alpine AS builder

WORKDIR /app

COPY pyproject.toml ./

COPY . .

RUN pip install --no-cache-dir build && python -m build --wheel

FROM python:3.13-alpine AS runner

WORKDIR /app

COPY --from=builder /app/dist/*.whl ./

RUN pip install --no-cache-dir *.whl

RUN rm -rf /app/build /app/*.egg-info

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

EXPOSE 8000

COPY scripts/buildprod.sh /app
RUN chmod +x /app/buildprod.sh

ENTRYPOINT ["/app/buildprod.sh"]
