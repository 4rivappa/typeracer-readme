
```
   __                                                    __      __       
  / /___  ______  ___  _________ _________  _____   ____/ /___ _/ /_____ _
 / __/ / / / __ \/ _ \/ ___/ __ `/ ___/ _ \/ ___/  / __  / __ `/ __/ __ `/
/ /_/ /_/ / /_/ /  __/ /  / /_/ / /__/  __/ /     / /_/ / /_/ / /_/ /_/ / 
\__/\__, / .___/\___/_/   \__,_/\___/\___/_/      \__,_/\__,_/\__/\__,_/  
   /____/_/                                                               
```


typeracer-readme generates typeracer graph for profile readme

<a href="">
  <img src="https://raw.githubusercontent.com/4rivappa/typeracer-readme/typeracer-readme/dark_graph.png" alt="typeracer graph" height="260"/>
</a>


# how it works
  getting data from typeracer with your username
  
  1000 at a time, looping until it gets all racing data
  
  generate two theme graphs (light and dark) images

# setup workflow
  copy script.py and requirements.txt into root directory of your repo
  
  copy typeracer_graph.yml yaml file into .github/workflows directory

# configure script.py
  username variable
   
  start_date variable (YYYY-MM-DD)
  
  average-window

# adding graph to readme
  add image with `src = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPOSITORY/typeracer-readme/dark_graph.png"`
   
  typeracer-readme above determines the branch in which images are saved
