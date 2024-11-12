import os
import pyheif
from PIL import Image

# HEIC 파일이 있는 폴더 경로
folder_path = '/app/your_folder'  # Docker 컨테이너 내 경로로 수정

# 폴더 내 모든 HEIC 파일을 변환
for file_name in os.listdir(folder_path):
    if file_name.lower().endswith('.heic'):
        heic_file_path = os.path.join(folder_path, file_name)
        output_file_path = os.path.join(folder_path, file_name.replace('.heic', '.jpg'))

        # HEIC 파일 읽기
        heif_file = pyheif.read(heic_file_path)

        # HEIC 파일을 Pillow 이미지 객체로 변환
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data, 
            "raw", 
            heif_file.mode, 
            heif_file.stride
        )

        # 이미지를 JPEG 형식으로 저장
        image.save(output_file_path, "JPEG")
        print(f"{file_name} 변환 완료!")



# 4. Docker 이미지 빌드
# 위에서 작성한 Dockerfile과 requirements.txt, convert_heic.py가 준비되었다면, 
# Docker 이미지를 빌드합니다.

# 터미널에서 Docker 이미지를 빌드합니다:

# bash
# Copy code
# docker build -t heic-converter .
# 5. Docker 컨테이너 실행
# Docker 이미지를 빌드한 후, HEIC 파일이 들어 있는 폴더를 컨테이너에 마운트하여 실행할 수 있습니다.

# bash
# Copy code
# docker run -v /path/to/your/folder:/app/your_folder heic-converter
# 여기서 /path/to/your/folder는 변환하려는 HEIC 파일이 있는 로컬 시스템의 경로입니다. 
# 이 경로는 Docker 컨테이너 내 /app/your_folder 디렉토리로 마운트됩니다.
