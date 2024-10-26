This small application shows how to inference with the Phi 3 Vision (Phi-3-vision-128k-instruct-onnx-cuda) model.
We do not use the transformers library here, we use the onnxruntime for GenAI. At the moment, opnnxruntime-genai is in preview.

Environment:

1. Ubuntu 24.04.1 LTS
2. DELL XPS 15 9530
3. Graphic Card (nvidia-smi ouput)
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

1. chmod +x setup.sh
2. ./setup.sh