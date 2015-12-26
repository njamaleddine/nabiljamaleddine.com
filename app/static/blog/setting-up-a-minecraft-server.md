<!-- # Setting up a Minecraft Server on Ubuntu 14.04 -->

If you're a minecraft enthusiast like myself you've probably spent countless hours building structures, spelunking, or just trying to survive a zombie raid through the night. If you're an avid fan and haven't already set up your own server to play with a couple of friends get on it.

## Requirements
[Ubuntu](http://www.ubuntu.com/) is a great option for setting up and running a minecraft server. Feel free to set it up on any other Linux distribution or Mac OS X, but keep in mind that there will be differences in set up.

If you don't have an available computer or you prefer to set up an online server, you can check out [Digital Ocean](https://www.digitalocean.com/?refcode=279f14897cf2) and sign up using the referral link. You're free to choose other hosting services though like Amazon EC2 or Rackspace.

## Digital Ocean Droplet Setup (Recommended)
If you chose Digital Ocean, it's recommended that your Ubuntu droplet (server) has at least 1GB of RAM with 2GB being optimal, but you might be able to manage at 512MB if approximately 4 people or less including yourself are on the server at once. If you have money to spend, you'll benefit from 1GB or more. More RAM will allow the minecraft server to be more performant and experience less lag and crashes from running out of memory.

For the purpose of this tutorial we're writing about Ubuntu 14.04 (64bit) since choosing a newer version might introduce slight differences in setup. Also 14.04 is the current LTS version at the time of this post.

Once you've chosen your droplet, you'll want to connect to the server using SSH. On Mac/Linux you can do this using the Terminal.

```bash
ssh user@ip_address
```

Your `ip_address` is your Digital Ocean server IP Address, and `user` is most likely `root` if you haven't modified any of the default setup.

Typing this in every time you want to connect to the server is annoying though, so instead you'll want to modify your ssh config on your personal computer.

Edit the following file `~/.ssh/config` by entering:

```bash
vim ~/.ssh/config
```

Add the droplet server to your config with your droplet IP Address (substitute 127.0.0.1):

```
Host minecraft
    HostName 127.0.0.1
    User root
```

Now you'll be able to enter your server by simply typing in:

```bash
ssh minecraft
```


## OS Setup
You'll want to make sure Ubuntu is up to date:

```bash
sudo apt-get update && sudo apt-get upgrade
```

You'll also want to check that java is installed

```bash
java -version
```

If java is not installed do so by entering:

```bash
sudo apt-get install default-jdk
```

## Minecraft Server Setup
You'll want to set up minecraft from the `srv` folder and make a minecraft folder there to store the minecraft server files. We'll do so by going into the `srv` folder

```bash
cd /srv
```

Make a minecraft directory:

```bash
mkdir minecraft
```

Now go into the Minecraft directory:

```bash
cd minecraft
```

You should now be in `/srv/minecraft`, check by entering `pwd` in the terminal.

Now that we've verified we're in the right folder, it's time to download the minecraft server software:

```bash
wget -O minecraft_server.jar https://s3.amazonaws.com/Minecraft.Download/versions/1.8.9/minecraft_server.1.8.9.jar
```

At the time of writing this post, the latest version of the Minecraft Server is `1.8.9` but check out [https://minecraft.net/download](https://minecraft.net/download)  to make sure you're downloading the most up to date version and modify the command above with the right version.

## Daemonize the Minecraft Server

To make sure that your server recovers from crashes and is always running you'll need to daemonize it. You can do so by adding an upstart script.

__Note__: If you are using a newer version of Ubuntu 14.04 you can still choose to use `upstart` instead of `systemd` which is the default in 15.04 and above, but this is out of the scope of this post. [More information on switching from systemd](https://wiki.ubuntu.com/SystemdForUpstartUsers)

### Setting up an upstart script
To daemonize the minecraft server you can create an upstart script.

Go to the following directory:

```bash
cd /etc/init/
```

Create the upstart script:

```bash
sudo vim minecraft-server.conf
```

Paste the following:

```
# description "start/stop minecraft-server"

start on runlevel [2345]
stop on runlevel [^2345]

console log
chdir /srv/minecraft

respawn
respawn limit 20 5

exec /usr/bin/java -Xms768M -Xmx768M -jar minecraft_server.1.8.9.jar nogui
```


**Important Note**

The last line will vary based on how much RAM you've allocated for your server. The part that reads `768M` dictates how much RAM to allocate to the minecraft server. This setup assumes you chose the 1GB option. Alternatively if you chose the 2GB option you would be able to allocate much more RAM. The first value, `-Xms768M`, is the minimum memory allocated, and the second, `-Xmx768M`, is the maximum allowed memory.

Now that your server upstart script is done reload the upstart configuration:

```bash
sudo initctl reload-configuration
```

And run your minecraft server

```bash
sudo start minecraft-server
```

## Final steps for server configuration
The last thing you need to do is sign the Minecraft EULA in the `eula.txt` file

Stop the minecraft server:

```bash
sudo stop minecraft-server
```

Edit the EULA:

```bash
vim /srv/minecraft/eula.txt
```

Set `eula=true`, then save/exit.


Restart the minecraft server.

```bash
sudo start minecraft-server
```

### Miscellaneous information
* Also check out you can modify the server properties by editing `/srv/minecraft/server.properties`

* Any changes you make on server files will require you to restart the minecraft server.

* If your server is crashing often or you chose a server with limited RAM (less than 1GB) you may need to allocate swap.

Congratulations, your server is now up and running. Go build some cool stuff.
