In today's lab we learned how to use our pi to send a receive messages to HiveMQ.
By subscribing to the proper topic in HiveMQ as well as on our RPi, in this lab
it was "ece631/Lab2Python/temperature/". By doing that we are able to send a
given message, in this lab we used a temperature value, have it be read by the
RPi, converted through a simple calculation and set back to HiveMQ for display.
In addition, we learned some of the basics of running screens display
information seen in HiveMQ on our RPi.

The code I used to implement the tasks described above is included in my 
Lab2Python repository.

    Important Commands to Remember:
        "sudo -i": switches to root user
        "exit": when in root returns to user
        "htop": opens process menu
        tab: autofills filenames
        "./filename": begins running file under the following name
        "screen -x": begins new screen under the running file
        "screen -r" filename: starts screen under given name
        "screen": begins new screen without name
        "screen -list": lists all open screens
    
        In screen commands:
        control+a: attaches to screen
        control+d: detaches from screen
        control+c: terminates process/current screen
        "k": will ask to terminate process