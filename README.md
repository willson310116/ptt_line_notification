# ptt_line_notification

### Abstract
This is a simple tool to get infomation from ptt and post to chosen line group automatically by executing this source code.

The source code utilizes *web crawler* and the service from *ifttt*

### Usage
1. set ifttt service
    - use **webhook** for If (trigger)
    - use **line** for Then (action)
![](https://i.imgur.com/4akanMb.png)
2. set for triggering event
    - get url from **documentation** of webhook
    ![](https://i.imgur.com/3mweb9f.png)
    - change {event} to your event name
    ![](https://i.imgur.com/HtKw9Uj.png)
    - copy the url and paste it in the source code
    ![](https://i.imgur.com/ZOtU3r3.png)
3. invite **Line Notify** to the chosen line group
4. execute the source code on terminal
```
python notify (the # of page you want to get) (forum name)
Ex: python notify 0 studyabroad
```
5. Line Notify will then post the title and url of the page you chose to the line group
![](https://i.imgur.com/apZrz1T.png)

***Note
This source code does not support forum with under 18 warning. 
Ex: gossiping***