#!/usr/bin/python

import vimeo

V = vimeo.VimeoClient(
    token="2d4cd3ab2357832659cf3424860da14f",
    key="b7423b6eaf753a63054398eb1266000a9ea10953",
    secret="Xx+B7Yr8LMia4zFSu8uVTyOSTb63Ljs0P8BgptQu8ZuxTgNKicIlU/1xZk2YUk+4dI4bIM0v8DLWt5FgpLwyGUT+E0dafhKo+4aMyhNmu5yb9R9po6hZam/2T1c1pr8V"
)

video_uri = V.upload('C:\Users\Sakuragi-Kun\Desktop\my.mp4')
