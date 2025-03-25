docker pull registry.cn-beijing.aliyuncs.com/quincyqiang/mineru:0.1-models
docker run -itd --name=mineru_server --gpus=all -p 8888:8000 docker.io/quincyqiang/mineru:0.1-models


# Blog:https://blog.csdn.net/yanqianglifei/article/details/141979684
# See http://localhost:8888/docs & http://127.0.01:8888/docs