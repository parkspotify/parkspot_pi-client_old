FROM balenalib/rpi-raspbian

# Install OpenCV build dependencies
RUN apt-get update && \
    apt-get install \
    python3-pip python3-dev python3-setuptools python3-numpy python3-scipy python3-requests python3-pil \
    build-essential \
    cmake \
    yasm \
    wget \
    unzip \
    pkg-config  \
    libtbb2 \
    libtbb-dev \
    libjpeg-dev \
    libtiff5-dev \
    libtiff-dev \
    libjasper-dev \
    libpng12-dev \
    libavformat-dev \
    libswscale-dev \
    libxvidcore-dev \
    libx264-dev \
    libatlas-base-dev \
    gfortran \
    libavcodec-dev \
    libv4l-dev \
    libpq-dev \
    libhdf5-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /
ENV OPENCV_VERSION="3.4.1"
RUN wget https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip && \
    unzip ${OPENCV_VERSION}.zip && \
    mkdir opencv-${OPENCV_VERSION}/cmake_binary && \
    cd opencv-${OPENCV_VERSION}/cmake_binary && \
    cmake \
    -DBUILD_TIFF=ON \
    -DBUILD_opencv_java=OFF \
    -DWITH_CUDA=OFF \
    -DWITH_OPENGL=ON \
    -DWITH_OPENCL=ON \
    -DWITH_IPP=ON \
    -DWITH_TBB=ON \
    -DWITH_EIGEN=ON \
    -DWITH_V4L=ON \
    -DBUILD_TESTS=OFF \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_PERF_TESTS=OFF \
    -DCMAKE_BUILD_TYPE=RELEASE \
    -DCMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") \
    -DPYTHON_EXECUTABLE=$(which python3) \
    -DPYTHON_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
    -DPYTHON_PACKAGES_PATH=$(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") .. && \
    make -j8 && \
    make install && \
    cd / && \
    rm -rf ${OPENCV_VERSION}.zip opencv-${OPENCV_VERSION}/

RUN pip3 --no-cache-dir install keras tensorflow numpy
