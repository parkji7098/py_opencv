import cv2, pafy, youtube_dl
url = 'https://www.youtube.com/watch?v=YpxMzU0F9lw'
video = pafy.new(url)

print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)

best = video.getbest()

print('best.resolution', best.resolution)

cap = cv2.VideoCapture(best.url)

cap.open(best.url)
while(cap.isOpened()):
    retval, frame = cap.read()
    if not retval:
        break
    cv2.imshow('frame',frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    edges = cv2.Canny(gray,200,100)
    cv2.imshow('edges',edges)
    
    key = cv2.waitKey(25)
    if key == 27:
        break
    
    
cv2.destroyAllWindows()



	
