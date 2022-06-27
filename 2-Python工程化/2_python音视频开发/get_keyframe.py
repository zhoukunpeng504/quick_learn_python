# coding:utf-8
__author__ = "zkp"
# create by zkp on 2022/6/26
# pyav - ffmpeg的python版封装。
# 学会通过pyav实时抽取关键帧并保存

import av


v_container = av.open("video.mp4", "r")  # 支持各种视频格式。支持智能识别编码
i = 0
for frame in v_container.decode(video=0):
    #print(dir(frame))
    if frame.key_frame:
        i += 1
        print(frame,i )
        frame.to_image().save('frame-%d.jpg' % i)
