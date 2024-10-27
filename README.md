This is a small test application that runs inference the phi-3-vision-128k-instruct model with onnxruntime-genai-cuda.

## Tested Environment

1. Ubuntu 24.04.1 LTS
2. DELL XPS 15 9530 with NVIDIA GeForce RTX 4060
3. Python 3.12

nvidia-smi output:  
<pre>
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.107.02             Driver Version: 550.107.02     CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4060 ...    Off |   00000000:01:00.0 Off |                  N/A |
| N/A   37C    P3            588W /   35W |       8MiB /   8188MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A      2963      G   /usr/lib/xorg/Xorg                              4MiB |
+-----------------------------------------------------------------------------------------+
</pre>

## Setup to get started:  
- Create a virtual environment in python (I used python 3.12, the venv module and poetry for dependency management)
- Run <code>setup.sh</code> in script folder to install all requirements. This installs all python packages (using poetry), downloads the phi model and installs cuda. 
- If everything is setup without errors, then run <code>python main.py</code>