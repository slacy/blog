Title: Resetting rows & columns after doing an import from G1 to G2
Date: 2005-09-07 00:21
Author: slacy
Category: Linux Stuff, Photos
Status: published

For my own reference more than anything else:

delete from g2\_PluginParameterMap where g\_pluginType='theme' and
g\_pluginId='matrix' and g\_parameterName='columns';

delete from g2\_PluginParameterMap where g\_pluginType='theme' and
g\_pluginId='matrix' and g\_parameterName='rows';
