FROM golang as builder

ENV GO111MODULE=on \
    CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64

WORKDIR /app

COPY cmd .
COPY go.mod .

RUN go build -o /app/bin/main .

FROM scratch

WORKDIR /app

COPY --from=builder /app/bin/main .
COPY index.html.format .

ENTRYPOINT ["/app/main"]