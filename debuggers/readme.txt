Java Debugger v1.8
(c) http://sevenuc.com

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
   # start JVM and attach debug server to it (suitable for server and GUI applications).
   $ java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=localhost:7001 -cp $CLASSPATH com.z.y.x.mainClass
   $ java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=localhost:7001 -cp $CLASSPATH -jar libx.jar
   $ java -jar sds.jar -sourcepath "/Users/username/full/path/of/project/src" -attach localhost:7001


Debugging Android Application

1. launch emulator → start "Dev Tools" app inside the emulator → "Development Settings",
   select your application as the "Debug App" → check on "Wait for debugger".

2. start the Dalvik Debug Monitor ("ddms" tool in the Android SDK), 
   this will allow debugger to connect to running apps inside the emulator or on a connected device.

3. Run your app inside the emulator, a message will prompt and say:
   "is waiting for the debugger to attach".

4. $ java -jar sds.1.0.0.jar -sourcepath "/Users/username/path/to/project/src" -attach localhost:8700
   INSTALL_FAILED_INSUFFICIENT_STORAGE
   To increase the size available to app, the emulator must be started with the
   “-partition-size” parameter. This command reserves 100MB for apps:
   emulator -partition-size 100 -avd <virtual-device-name>


This debugger should work with all kinds of JVM that implemented Java Debugger API, 
JDK all version from 6 and later in theory.


Jul 13 2021


