import os
os.system(f"git lfs install")
os.system(f"git clone -b v1.3 https://github.com/camenduru/ComfyUI /home/demo/source/ComfyUI")
os.chdir(f"/home/demo/source/ComfyUI")
os.system(f"pip install -r requirements.txt")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth -d /home/demo/source/ComfyUI/models/upscale_models -o RealESRGAN_x2plus.pth")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://dagshub.com/sdxl/stable-diffusion-xl-base-0.9/raw/d82c04e3c1866d98718a4c0f7d91392bcd3e0bcd/data/sd_xl_base_0.9.safetensors -d /home/demo/source/ComfyUI/models/checkpoints -o sd_xl_base_0.9.safetensors")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://dagshub.com/sdxl/stable-diffusion-xl-refiner-0.9/raw/e7aa1d4794e5c84e1f3940ff082a61be751432ef/data/sd_xl_refiner_0.9.safetensors -d /home/demo/source/ComfyUI/models/checkpoints -o sd_xl_refiner_0.9.safetensors")
os.system(f"python main.py --dont-print-server --port 8266 --enable-cors-header")
