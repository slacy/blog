Title: Extremely simple XML to Python converter
Date: 2011-03-01 17:51
Author: slacy
Category: General
Tags: converter, mongodb, python, xml, xml to python
Status: published

There are a ton of different ways you can encode XML, but for the style
that looks like this:

    <xml> 
    <name>Bob</name> 
    ...

You can use this nice little function to convert it to a native Python
object.  I'm using this to turn the results of the LinkedIn API from XML
to Python, which then gets stored as JavaScript in MongoDB.

Set "force\_list" to a list of field names that you know are list-values
and it will convert those to lists in Python.  Yeah, that could be
cleaner and more automatic.  Not really that proud of this, but it does
work...

    import xml.dom.minidom

    def typeconvert(str_data):
        try:
            int_value = int(str_data)
            return int_value
        except:
            pass
        try:
            float_value = float(str_data)
            return float_value
        except:
            pass

        if str_data.lower() == 'false':
            return False
        if str_data.lower() == 'true':
            return True
        if str_data.lower() == 'null':
            return None

        return str_data

    def xml_to_py(xml_text, force_list=[], convert_types=True):

        def setval(data, key, value):
            if key in force_list:
                if key not in data:
                    data[key] = []
                data[key].append(value)
            else:
                if key in data:
                    logging.warn("WARN: key %s, value %s in XML seems like a list" % (key, value))
                    pass
                data[key] = value

        def recurse(node):
            nodename = node.nodeName
            result = {}
            if node.nodeType == xml.dom.Node.TEXT_NODE:
                nodetext = node.data.strip(' \n')
            else:
                nodetext = ''
            for child in node.childNodes:
                if child.nodeType == xml.dom.Node.TEXT_NODE:
                    nodetext += child.data.strip(' \n')
                else:
                    (newtext, newdata) = recurse(child)
                    if newtext and newdata:
                        raise Exception("Can't have both text and data")
                    if newtext != '':  # newtext could be an integer with value 0
                        if convert_types:
                            newtext = typeconvert(newtext)

                        setval(result, child.nodeName, newtext)
                    elif newdata:
                        setval(result, child.nodeName, newdata)

            return (nodetext, result)

        dom = xml.dom.minidom.parseString(xml_text)
        (_text, pydict) = recurse(dom)
        return pydict
