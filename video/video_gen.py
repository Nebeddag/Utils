import cv2
import ntpath
from datetime import timedelta

class FrameGenerator:
    def __init__(self, files_dates, span_sec, frame_rate=None) -> None:
        self.files_dates = files_dates
        self.span_sec = span_sec
        self.frame_rate = frame_rate

    def generator(self):
        for fl, dt in self.files_dates:
            video_name = ''
            try:
                video_name = ntpath.basename(fl)
                video_name = video_name[0:video_name.rfind('.')]
                video_name = video_name.replace(' ', '_')

                # process video
                cap = cv2.VideoCapture(fl)
                frame_rate = cap.get(5) # frame rate

                if self.frame_rate:
                    frame_rate = self.frame_rate

                frame_span = round(frame_rate * self.span_sec)
                frames_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

                if frame_span == 0:
                    print(f'video {video_name} is broken!')
                    continue

                for frame_num in range(int(frames_count // frame_span)):
                    try:
                        if not cap.isOpened():
                            break

                        frame_id = int(frame_num * frame_span)

                        cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_id))
                        ret, frame = cap.read()
                        if (ret != True):
                            break

                        frame_time = dt + timedelta(seconds=frame_id/frame_rate)

                        yield frame, frame_id, frame_time
                        
                    except Exception as e:
                        print(e)
                cap.release()
            except:
                print(f'video {video_name} is broken!')