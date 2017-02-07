Title: Android: Assistive Technology not found or SWT.error trying to run ddms
Date: 2010-04-08 12:09
Author: slacy
Category: General
Tags: android, ddms, sdk
Status: published

If you're trying to run ddms from the Android SDK and you get this
error:

    06:24 E/ddms: shutting down due to uncaught exception
    06:24 E/ddms: java.awt.AWTError: Assistive Technology not found: org.GNOME.Accessibility.JavaBridge

OR

    08:53:11 E/ddms: shutting down due to uncaught exception
    08:53:11 E/ddms: org.eclipse.swt.SWTError: Not implemented [multiple displays]
        at org.eclipse.swt.SWT.error(Unknown Source)
        at org.eclipse.swt.widgets.Display.checkDisplay(Unknown Source)
        at org.eclipse.swt.widgets.Display.create(Unknown Source)
        at org.eclipse.swt.graphics.Device.<init>(Unknown Source)
        at org.eclipse.swt.widgets.Display.<init>(Unknown Source)
        at org.eclipse.swt.widgets.Display.<init>(Unknown Source)
        at com.android.ddms.UIThread.runUI(UIThread.java:419)
        at com.android.ddms.Main.main(Main.java:105)

Then you can fix it via:

\$ sudo apt-get install openjdk-6-jre

You're welcome. :)
