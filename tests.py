import cv2
from video.frame_iterator import FramesIterator

fn = 'D:\Films\Chungking Express (1994)\Chungking.Express.1994.BDRip.x264.AAC.Rus.Eng.Comm.Sub.tRuAVC.mkv'
fr_iter = FramesIterator(fn, from_sec=60, span_sec=600)

for frame, frame_id, frame_time in fr_iter:
    cv2.imshow(f'frame:{frame_id} time:{str(frame_time)}' , frame)
    cv2.waitKey()
