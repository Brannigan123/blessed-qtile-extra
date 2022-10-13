# A collection of my custom qtile bar widgets


https://user-images.githubusercontent.com/41282933/195697101-8583f7aa-e086-451b-b2a2-16c5b2df5e46.mp4



## VisualizerBars widget
Renders cava visualizer's output to the qtile bar

| Parameter   | Default                           | Description                              |
| ----------- | --------------------------------- | ---------------------------------------- |
| pipe        | ~/.config/qtile/.gen/cava.fifo    | Pipe where cava should dump ascii output |
| config_dump | '~/.config/qtile/.gen/cava.config | Where to dumps config to be used by cava |
| frequency   | 60                                | The poll frequency                       |
| bars        | ▁▂▃▄▅▆▇█                           | Characters used to draw the bars         |
| bar_count   | 10                                | Number of bars                           |
        
## AppName widget
A qtile bar widget that just displays the name of focused application.

| Parameter    | Default                           | Description                              |
| ------------ | --------------------------------- | ---------------------------------------- |
| default_name |                                   | Name to use incase none is detected      |
| format       | '{name}'                          | format of the text                       |
