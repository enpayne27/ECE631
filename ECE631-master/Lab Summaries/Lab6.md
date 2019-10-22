In today's lab we learned how to utilize the serial monitor to send and receive
characters from the Arduino IDE to the STM32 Discovery board using circular buffers. 
Rather than using the included buffer system in the STM32 library, we were able
to build our own circular buffers to avoid the overflow corruptions.Once again I
had to use the following process to upload my code to the Discovery board.

Go into the Project Explorer and right click:
Clean project>Build Project>Target>Program chip

Then click the black reset button on the board and your most recent code should run.

Additionally to access the serial monitor through the Arduino IDE I performed the
following to refresh the serial monitor with every new build of my code:
Tools>Serial Monitor