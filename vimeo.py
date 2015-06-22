#!/usr/bin/python

import vimeo

V = vimeo.VimeoClient(
    token="2d4cd3ab2357832659cf3424860da14f",
    key="b7423b6eaf753a63054398eb1266000a9ea10953",
    secret="Xx+B7Yr8LMia4zFSu8uVTyOSTb63Ljs0P8BgptQu8ZuxTgNKicIlU/1xZk2YUk+4dI4bIM0v8DLWt5FgpLwyGUT+E0dafhKo+4aMyhNmu5yb9R9po6hZam/2T1c1pr8V"
)
about_me = V.get('https://vimeo.com/home/myvideos')

assert about_me.status_code == 200
# print about_me.json()

vimeo_authorization_url = V.auth_url(['public'], ['private'], 'https:example.com')

video_uri = V.upload('F:\photoes\Mobile camera/video-2014-09-21-11-13-58.mp4')
