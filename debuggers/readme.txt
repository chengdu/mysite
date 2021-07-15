-------------------------------------------------------
Java Debugger v1.8
(c) http://sevenuc.com
-------------------------------------------------------

This is the Java remote debugger for Speare code editor
http://www.sevenuc.com/en/speare.html

Package source: 
http://www.sevenuc.com/debuggers/java_debugger.zip

Directory Structure:
java_debugger
|____sds.jar        # the debugger, executable jar file
|____readme.txt     # readme for this package

Start Java debugging session:
1. Setup environment variable for JAVA_HOME and CLASSPATH
   $ export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_171.jdk/Contents/Home
   $ export PATH=$JAVA_HOME/bin:$PATH
   $ export CLASSPATH=.:$JAVA_HOME/lib:$CLASSPATH

2. Compile source code with -g

3. Start debug server
   Launch approach A: 
   # directly start JVM with debug server (suitable for standalone non-GUI library or applications).
   $ java -jar sds.jar -sourcepath "/Users/username/full/path/of/project/src" -cp $CLASSPATH com/z/y/x/mainClass
     (using class files: sds.jar and folder "com/z/y/x/..." both should be under the same directory)
   $ java -jar sds.jar -sourcepath "/Users/username/full/path/of/project/src" -cp $CLASSPATH -jar libx.jar
     (using jar file directly)

   Launch approach B: 
   # start JVM and attach debug server to it (suitable for server, Android, and GUI applications).
   $ java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=localhost:7001 -cp $CLASSPATH com/z/y/x/mainClass
   $ java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=localhost:7001 -cp $CLASSPATH -jar app.jar
   $ java -jar sds.jar -sourcepath "/Users/username/full/path/of/project/src" -attach localhost:7001

Debugging Android Application
1. launch emulator → start "Dev Tools" app inside the emulator → "Development Settings",
   select your application as the "Debug App" → check on "Wait for debugger".

2. start the Dalvik Debug Monitor ("ddms" tool in the Android SDK), 
   this will allow debugger to connect to running apps inside the emulator or on a connected device.

3. Run your app inside the emulator, a message will prompt and say:
   "is waiting for the debugger to attach".

4. $ java -jar sds.jar -sourcepath "/Users/username/path/to/project/src" -attach localhost:8700
   INSTALL_FAILED_INSUFFICIENT_STORAGE
   To increase the size available to app, the emulator must be started with the
   “-partition-size” parameter. This command reserves 100MB for apps:
   emulator -partition-size 100 -avd <virtual-device-name>

   Details Explained
   -----------------------------
   In order to attach debugger to an Android application, which is running inside the Dalvik VM, we have to use adb bridges 
   the gap between an application and a development/debugging environment. The Dalvik VM creates a JDWP thread for every 
   application to allow debuggers to attach to it on certain ports/process IDs. In order to find out the JDWP port of a 
   debuggable application, run the command:

   $ adb jdwp

   This will return a list of currently active JDWP processes, the very last number corresponds to the last debuggable 
   application launched. To attach debugger to the remote VM we have to have adb forward the remote JDWP port to a local port. 
   This is done with the forward command, like so: 

   $ adb forward tcp:7001 jdwp:JDWP_PORT

   adb will open a local TCP socket that you can connect to, and will forward all data sent to the local TCP socket to the JDWP 
   process running on the device/emulator. After forward data, attach debugger like normal:

   $ java -jar sds.jar -sourcepath "/Users/username/full/path/of/project/src" -attach localhost:7001
   -----------------------------

Debugging Server Applications
1. Settings to launch Tomcat applications
   The startup script for Tomcat is named catalina.sh, to start a server with debug arguments:
   $ catalina.sh jpda start
   The default listening on port is 8000 and suspend=n, them can be changed by environment variables: 
   JPDA_TRANSPORT, JPDA_ADDRESS, and JPDA_SUSPEND.

2. Settings to launch Spring applications
   a. launch application from the command line with debug arguments:
      $ java -jar myapp.jar -Dagentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=7001

   b. Maven:
      $ mvn spring-boot:run -Dagentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=7001

   c. Gradle: 
      * ensure Gradle passes command line arguments to the JVM:
        bootRun {
           systemProperties = System.properties
        }
      $ gradle bootRun -Dagentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=7001

3. Weblogic
   The startup script for Weblogic is startWeblogic.sh, to start a server with debug enabled just set the 
   environment variable debugFlag to true. The default listener on port is 8453 and suspend=n, can override
   by setting the DEBUG_PORT environment variable.

4. WebSphere
   Check the startup script for WebSphere and find debug option and env variables to setup JVM debug enabled,
      WAS_DEBUG
      -J <java_option>
      -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=7001

   check points:
   0. don't configure debug options on web page.
   a. /WebSphere/AppServer/bin/startServer.sh
   b. /WebSphere/AppServer/profiles/WRSProfile/config/cells/WRSNodeCell/nodes/WRSNode/servers/server1/server.xml
   c. associated service for the profile with 'manual' mode.
   d. stop and start the server.

5. JBoss (Wildfly)
   The startup script for JBoss is stand-alone.sh, to start a server with debug enabled just add –debug.
   The default listener on port is 8787 and suspend=n, can be override by specifying it after –debug argument.

6. Glassfish
   The startup script for Glassfish is asadmin, to start a server with debug enabled just add –debug:
   $ asadmin start-domain --debug
   The default listener on port is 9009 and suspend=n.


7. Jetty
   To start a Jetty application server just add debug arguments to java command:
   -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=7001


This debugger provide support for multithreaded programs and remote applications, lightweight and fast, 
should work with all kinds of JVM that implemented Java Debugger API, JDK all version from 6 and later.


Jul 13 2021


