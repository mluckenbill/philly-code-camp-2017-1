First update package list
sudo apt-get update

You now need to unpack the tar.qz using the code

tar zxvf motion-mmal.tar.gz
Once unpacked you will need to make changes to the config file using

sudo nano motion-mmalcam.conf
You will then need to make changes to the following settings

Turn deamon to On
stream_localhost to Off
By switch the steam_localhost you will be able to access the cameras webpage (port 8080 by default) and web configuration page (port 8081 by default) on any other device on your network. Once done save the config file with Ctrl+X and type Y to save the edited config file

Make motion executable
sudo chmod motion +x

To run the program enter the command

sudo ./motion -c motion-mmalcam.conf
If you have issues with running the program enter the command

sudo apt-get install libjpeg62