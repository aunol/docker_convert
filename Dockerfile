# Python 3.11 이미지 기반
FROM python:3.11-slim

# 시스템 패키지 업데이트 및 필수 라이브러리 설치 (HEIF 변환을 위한 라이브러리)
RUN apt-get update && apt-get install -y \
    libheif-dev \
    libjpeg-dev \
    libimage-exiftool-perl \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /app

# 필요 라이브러리 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 스크립트 파일 복사
COPY . /app

# 실행할 Python 스크립트 지정
CMD ["python", "convert_heic.py"]
