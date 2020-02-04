from xml.etree import ElementTree
from pprint import pprint


def tree_of_xml(str):
    tree = ElementTree.XML(str)
    pprint(pars(tree))


def pars(elem, depth=-1):
    dict = {"name": elem.tag}
    dict.update({"children": []})
    for child in list(elem):
        dict["children"].append(pars(child, depth)[0])
        depth += 1
    return dict, depth


a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
tree_of_xml(a)