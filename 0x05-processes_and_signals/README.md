# Welcome to 0x05-processes_and_signals
In this project we will practice a little bit about processes and signals

| Task | Description |
| ---- | ----------- |
| 0-what-is-my-pid   | script that displays its own PID |
| 1-list_your_processes | script displays a list of currently running processes |
| 2-show_your_bash_pid | script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process |
| 3-show_your_bash_pid_made_easy | script that displays the PID, along with the process name, of processes whose name contain the word bash |
| 4-to_infinity_and_beyond | script that displays To infinity and beyond indefinitely |
| 5-dont_stop_me_now | script that stops 4-to_infinity_and_beyond process |
| 6-stop_me_if_you_can |  script that stops 4-to_infinity_and_beyond process |
| 7-highlander | script displays To infinity and beyond indefinitely, With a sleep 2 in between each iteration, I am invincible!!! when receiving a SIGTERM signal |
| 8-beheaded_process | script that kills the process 7-highlander |
| 100-process_and_pid_file | script that: <br/> * Creates the file /var/run/myscript.pid containing its PID <br/> * Displays To infinity and beyond indefinitely <br/> * Displays I hate the kill command when receiving a SIGTERM signal <br/> * Displays Y U no love me?! when receiving a SIGINT signal <br/> * Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal |

