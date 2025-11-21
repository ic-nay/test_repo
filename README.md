Testing out just making a straight Flask app to see if I can serve anything at all



# Video Server
Unfortunately, there aren't any publicly accessible RSTP streams, so we'll have to make out own.
1. We're using MediaMTX to serve an RSTP stream, so download a binary of that: https://github.com/bluenviron/mediamtx/releases
2. You'll also need ffmpeg, so be sure to have that installed as well.
3. Then, run the following commands, replacing PATH_TO_VIDEO with a video you want to stream
```
./mediamtx
ffmpeg -stream_loop -1 -i "PATH_TO_VIDEO" -f rtsp rtsp://localhost:8554/live.sdp
```