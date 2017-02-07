Title: Jenkins workspace archiving breaks on symlinks.
Date: 2012-04-17 12:20
Author: slacy
Category: General
Status: published

Our Jenkins build was working great (archiving one workspace, and then
untarring it into another using the Archive for Clone Workspace feature)
and then one day it broke.

The error was in the second build job, and says:

       at hudson.model.Run.run(Run.java:1421)
        at hudson.model.FreeStyleBuild.run(FreeStyleBuild.java:46)
        at hudson.model.ResourceController.execute(ResourceController.java:88)
        at hudson.model.Executor.run(Executor.java:238)
    Caused by: java.io.IOException: Failed to chmod /var/lib/jenkins/jobs/oswebsite_test/workspace/wsve/lib/python2.6/UserDict.py : Operation not permitted
        at hudson.FilePath._chmod(FilePath.java:1248)
        at hudson.FilePath.readFromTar(FilePath.java:1813)
        ... 16 more

The issue is [Jenkins Bug
13280](https://issues.jenkins-ci.org/browse/JENKINS-13280) which
basically says that the "Archive for Clone Workspace" feature is broken
if your workspace contains symlinks.  Hopefully that bug will be fixed
soon.

My workaround was to just set a "custom workspace directory" for the
second job to be the workspace directory of the first job.  Not a clean
solution, but it gets things done.
