ARG PYTORCH="1.13.0"
ARG CUDA="11.6"
ARG CUDNN="8"

FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-devel

ENV TORCH_CUDA_ARCH_LIST="6.0 6.1 7.0+PTX"
ENV TORCH_NVCC_FLAGS="-Xfatbin -compress-all"
ENV CMAKE_PREFIX_PATH="$(dirname $(which conda))/../"
ENV FORCE_CUDA="1"


# To fix GPG key error when running apt-get update
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub

RUN apt-get update && apt-get install -y unzip git sudo ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 libgl1-mesa-glx wget ffmpeg\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# create a non-root user
ARG USER_ID=1000
RUN useradd -m --no-log-init --system  --uid ${USER_ID} appuser -g sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER appuser

ENV HOME=/home/appuser
WORKDIR $HOME
ENV PATH="/home/appuser/.local/bin:${PATH}"
ENV PYTHONPATH="/home/appuser:$PYTHONPATH"



# Install Jupyter
RUN pip install --user --upgrade pip
RUN pip install --user traitlets jinja2 ipython
RUN pip3 install --user jupyter notebook  



WORKDIR /work
RUN sudo chmod -R 777 /work
ENV PYTHONPATH=/work:$PYTHONPATH

WORKDIR /work
COPY requirements.txt .
RUN pip install -r requirements.txt


# CMD ["bash"]
CMD ["jupyter", "notebook", "--port=8888", "--ip=0.0.0.0", "--allow-root"]
